# 🧠 Second Brain: Job Application Workflow

A structured personal knowledge repository designed to manage your professional experience, education, projects, and interview preparation. It features machine-readable instructions for AI agents and an automated toolchain to compile clean, tailored, single-page resumes and cover letters.

---

## ⚡ Quick Start (AI Agent Setup)

Copy and paste this prompt into a new chat with your AI assistant (e.g. Claude or Gemini) to set up your repository in seconds:

```text
I want to set up my job application workflow using the Second Brain template. Please clone or fetch the files from https://github.com/ShahirShamim/Job-Application-Workflow, read the setup.md file in that repository, and follow its step-by-step instructions to initialize the workspace with my professional history. I will provide my resume now.
```

---

## 🌟 Why Use This?

- **Single Source of Truth**: Keep your entire career history, achievements, and metrics in one place.
- **AI-Agent Native**: Includes detailed guidelines and a setup routine that allows LLM agents to manage and update your files, tailor applications, and parse incoming jobs.
- **Automated Formatting**: A Python script uses **Playwright** to compile print-optimized HTML resumes and cover letters into A4 PDFs. It features an **auto-fitting loop** that dynamically scales font size to ensure tailored documents fit exactly on a single page.

---

## 📁 Directory Structure

```text
Job Application Workflow/
├── Employment/
│   ├── past.md           # Completed professional roles & achievements
│   ├── present.md        # Active roles & current tasks
│   ├── future.md         # Career goals & target roles
│   ├── applied.md        # Job application tracker
│   ├── interview_prep.md # STAR stories for behavioral interviews
│   ├── references.md     # Reference sheet for supervisors & peers
│   ├── resume.html       # Master baseline resume (HTML/CSS)
│   └── tailored_resumes/ # Workspace for active job applications
│       ├── resume-pdfs/  # Output folder for generated resume PDFs
│       ├── coverletter-pdfs/ # Output folder for generated cover letter PDFs
│       └── cover_letters/ # Tailored HTML cover letters & plain text outreach
├── Education/
│   ├── past.md           # Degrees, honors, thesis work, and coursework
│   ├── present.md        # Active courses & ongoing self-study
│   └── future.md         # Future certifications & topics
├── Projects/
│   ├── past.md           # Completed code repositories & side projects
│   ├── present.md        # Active development projects
│   ├── future.md         # Backlog of ideas & product drafts
│   └── system_designs.md # Architectural diagrams & notes
├── consume/              # Inbox for inbound job specifications (dropped here)
│   └── jobs/
├── archive/              # Processed records & historical resumes
│   ├── jobs/
│   └── tailored_resumes/
├── skills_matrix.md      # Tech skills & PM methodologies map
├── metrics_repository.md # Metrics database mapping impact to roles
├── agents.md             # Guidelines for AI agents interacting with this repo
├── setup.md              # Onboarding guide for AI agents to populate your files
└── README.md             # This file
```

---

## 🚀 Getting Started

The easiest way to initialize this repository and install required tools is using an AI agent (like Claude or Gemini).

1. Create a new chat session with your AI assistant.
2. Share the [setup.md](./setup.md) file and your current resume (PDF, HTML, or plain text).
3. The agent will read `setup.md`, automatically install all necessary dependencies (like Playwright and other rendering packages), parse your resume, and populate the templates across the repository.

---

## 🔄 Daily Workflow

### Phase 1: Keep It Updated
As you complete tasks, build side projects, or achieve metrics, you don't need to update all tables manually. Simply describe what you did to your AI assistant (e.g., "I finished a Python project optimizing delivery routes by 15%"). 

The agent will read [agents.md](./agents.md) and automatically:
- Log details in `Employment/present.md` or `Projects/present.md`.
- Sync new achievements and skills directly to the master [resume.html](./Employment/resume.html).
- Archive old roles into `past.md` and append metrics to [metrics_repository.md](./metrics_repository.md).
- Update the [skills_matrix.md](./skills_matrix.md).

### Phase 2: Tailoring to a Job
When you find a job you want to apply to:
1. Drop the job spec text into `consume/jobs/` (e.g. `spec_Company_Role.txt`).
2. Ask your AI agent to review the spec and match it against your `past.md` and `skills_matrix.md`.
3. The agent will:
   - Create a tailored resume in `tailored_resumes/` named `resume_[Company]_[Role]_[Month]_[Year].html`.
   - Write a matching cover letter in `tailored_resumes/cover_letters/` named `cover_letter_[Company]_[Role]_[Month]_[Year].html`.
   - Ensure the content is selected and pruned to fit on exactly **1 A4 page**.

### Phase 3: Compile to PDF
Compile the master resume or all active tailored documents:

```bash
# Compile everything (master resume + tailored html files + cover letters)
python Employment/generate_pdf.py

# Compile a specific tailored resume to a custom location
python Employment/generate_pdf.py --input Employment/tailored_resumes/resume_Company_Role_June_2026.html

# Compile with a forced max page limit (e.g., forcing a 1-page limit)
python Employment/generate_pdf.py --input Employment/tailored_resumes/resume_Company_Role_June_2026.html --max-pages 1
```

*Note: The script automatically runs a loop reducing CSS scale (from `1.0` down to `0.5`) until the rendered HTML fits within the specified page limit, avoiding ugly line-wraps or page overflows.*

### Phase 4: Apply & Archive
1. Once you apply, log it in [applied.md](./Employment/applied.md).
2. Clean up your workspace by moving the HTML and PDF resumes/cover letters from `tailored_resumes/` to `archive/tailored_resumes/` (maintaining folder layout).
3. Move the job spec from `consume/jobs/` to `archive/jobs/`.
