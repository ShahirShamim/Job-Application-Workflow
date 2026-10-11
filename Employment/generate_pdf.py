#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import tempfile
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

# Default directories
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TAILORED_DIR = os.path.join(SCRIPT_DIR, "tailored_resumes")
PDF_DIR = os.path.join(TAILORED_DIR, "resume-pdfs")

def get_page_count(pdf_path):
    """Returns the page count of the PDF at pdf_path."""
    try:
        reader = PdfReader(pdf_path)
        return len(reader.pages)
    except Exception as e:
        print(f"Error reading PDF page count: {e}", file=sys.stderr)
        return 0

def render_pdf(page, file_url, pdf_path, scale):
    """Renders the HTML file_url to pdf_path with the given scale."""
    page.pdf(
        path=pdf_path,
        format="A4",
        scale=scale,
        print_background=True,
        prefer_css_page_size=True
    )

def process_file(page, html_path, pdf_path, target_pages=1, manual_scale=None, auto_fit=True):
    """Loads the HTML file, renders to PDF, and runs the scale loop if auto_fit is enabled."""
    absolute_html = os.path.abspath(html_path)
    file_url = f"file://{absolute_html}"
    
    page.goto(file_url)
    page.wait_for_load_state("networkidle")
    
    if manual_scale is not None:
        print(f"Rendering {os.path.basename(html_path)} with manual scale: {manual_scale}")
        if manual_scale < 0.75:
            print(f"  → Manual scale {manual_scale:.2f} is below 0.75. Injecting margin and layout spacing adjustments...")
            page.add_style_tag(content="""
                @page { margin: 0.25in 0.35in !important; }
                body { padding: 0.25in 0.35in !important; line-height: 1.05 !important; }
                .job-block { margin-bottom: 4px !important; }
                ul { padding-left: 1.0em !important; }
                h2 { margin-top: 8px !important; margin-bottom: 4px !important; }
            """)
        render_pdf(page, file_url, pdf_path, manual_scale)
        pages = get_page_count(pdf_path)
        print(f"Saved: {pdf_path} (Pages: {pages})")
        return
        
    scale = 1.0
    temp_pdf = None
    margins_adjusted = False
    
    try:
        # Use a temporary file to check page count during the scale fitting loop
        fd, temp_pdf = tempfile.mkstemp(suffix=".pdf")
        os.close(fd)
        
        while scale >= 0.5:
            if auto_fit and scale < 0.75 and not margins_adjusted:
                print(f"  → Scale fell below 0.75. Injecting margin and layout spacing adjustments...")
                page.add_style_tag(content="""
                    @page { margin: 0.25in 0.35in !important; }
                    body { padding: 0.25in 0.35in !important; line-height: 1.05 !important; }
                    .job-block { margin-bottom: 4px !important; }
                    ul { padding-left: 1.0em !important; }
                    h2 { margin-top: 8px !important; margin-bottom: 4px !important; }
                """)
                margins_adjusted = True
                
            render_pdf(page, file_url, temp_pdf, scale)
            pages = get_page_count(temp_pdf)
            
            if not auto_fit or pages <= target_pages:
                # Target achieved or auto-fit disabled, write to final destination
                shutil.move(temp_pdf, pdf_path)
                temp_pdf = None
                print(f"✓ Saved: {os.path.basename(pdf_path)} (Pages: {pages}, Scale: {scale:.2f})")
                return
            
            # Decrement scale factor and retry
            scale -= 0.02
            
        # If we broke out of loop and still didn't fit, write the lowest scale result
        if temp_pdf and os.path.exists(temp_pdf):
            shutil.move(temp_pdf, pdf_path)
            temp_pdf = None
            print(f"⚠ Warning: Content could not fit in {target_pages} page(s) at minimum scale (0.50). "
                  f"Saved at scale 0.50: {os.path.basename(pdf_path)}")
                  
    finally:
        if temp_pdf and os.path.exists(temp_pdf):
            try:
                os.remove(temp_pdf)
            except OSError:
                pass

def main():
    parser = argparse.ArgumentParser(description="Compile HTML resumes to A4 PDFs with auto-fitting.")
    parser.add_argument("--input", help="Path to specific HTML resume. If omitted, scans for all resumes.")
    parser.add_argument("--output", help="Output PDF path. Only valid when --input is provided.")
    parser.add_argument("--max-pages", type=int, default=1, help="Target maximum page count (default: 1).")
    parser.add_argument("--scale", type=float, help="Manual scale factor override (0.1 to 2.0).")
    parser.add_argument("--no-auto-fit", action="store_true", help="Disable the auto-fitting scale loop.")
    
    args = parser.parse_args()
    
    # Ensure PDF output directory exists
    os.makedirs(PDF_DIR, exist_ok=True)
    
    # Determine files to process
    jobs = []
    if args.input:
        if not os.path.exists(args.input):
            print(f"Error: Input file '{args.input}' does not exist.", file=sys.stderr)
            sys.exit(1)
            
        if args.output:
            out_pdf = args.output
        else:
            base_name = os.path.splitext(os.path.basename(args.input))[0]
            if base_name in ("resume", "cover_letter", "resume_consulting"):
                out_pdf = os.path.join(SCRIPT_DIR, f"{base_name}.pdf")
            else:
                out_pdf = os.path.join(PDF_DIR, f"{base_name}.pdf")
        jobs.append((args.input, out_pdf))
    else:
        # Default: Process baseline resume.html, baseline cover_letter.html and all HTMLs in tailored_resumes/
        baseline_html = os.path.join(SCRIPT_DIR, "resume.html")
        if os.path.exists(baseline_html):
            jobs.append((baseline_html, os.path.join(SCRIPT_DIR, "resume.pdf")))
            
        baseline_cover = os.path.join(SCRIPT_DIR, "cover_letter.html")
        if os.path.exists(baseline_cover):
            jobs.append((baseline_cover, os.path.join(SCRIPT_DIR, "cover_letter.pdf")))

        baseline_consulting = os.path.join(SCRIPT_DIR, "resume_consulting.html")
        if os.path.exists(baseline_consulting):
            jobs.append((baseline_consulting, os.path.join(SCRIPT_DIR, "resume_consulting.pdf")))
            
        if os.path.exists(TAILORED_DIR):
            for file in os.listdir(TAILORED_DIR):
                if file.endswith(".html"):
                    html_path = os.path.join(TAILORED_DIR, file)
                    base_name = os.path.splitext(file)[0]
                    pdf_path = os.path.join(PDF_DIR, f"{base_name}.pdf")
                    jobs.append((html_path, pdf_path))
                    
            # Process cover letters
            cover_letters_dir = os.path.join(TAILORED_DIR, "cover_letters")
            cover_letters_pdf_dir = os.path.join(TAILORED_DIR, "coverletter-pdfs")
            if os.path.exists(cover_letters_dir):
                os.makedirs(cover_letters_pdf_dir, exist_ok=True)
                for file in os.listdir(cover_letters_dir):
                    if file.endswith(".html"):
                        html_path = os.path.join(cover_letters_dir, file)
                        base_name = os.path.splitext(file)[0]
                        pdf_path = os.path.join(cover_letters_pdf_dir, f"{base_name}.pdf")
                        jobs.append((html_path, pdf_path))
                    
    if not jobs:
        print("No HTML resumes found to process.")
        sys.exit(0)
        
    print(f"Initializing PDF generation for {len(jobs)} resume(s)...")
    
    with sync_playwright() as p:
        # Launch Chromium headless browser
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        for html_path, pdf_path in jobs:
            try:
                is_resume_baseline = os.path.basename(html_path) == "resume.html"
                is_consulting_baseline = os.path.basename(html_path) == "resume_consulting.html"
                is_cover_baseline = os.path.basename(html_path) == "cover_letter.html"
                is_baseline = is_resume_baseline or is_consulting_baseline or is_cover_baseline
                
                target_pages = args.max_pages
                if (is_resume_baseline or is_consulting_baseline) and "--max-pages" not in sys.argv:
                    target_pages = 10
                elif is_cover_baseline and "--max-pages" not in sys.argv:
                    target_pages = 1
                
                process_file(
                    page=page,
                    html_path=html_path,
                    pdf_path=pdf_path,
                    target_pages=target_pages,
                    manual_scale=args.scale,
                    auto_fit=not (args.no_auto_fit or is_baseline)
                )
            except Exception as e:
                print(f"Error processing {os.path.basename(html_path)}: {e}", file=sys.stderr)
                
        browser.close()

if __name__ == "__main__":
    main()
