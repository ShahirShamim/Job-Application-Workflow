# 🧠 Second Brain Agent Guide

Guide for AI agents (Gemini/Claude/Codex) in this directory. Define intent, structure, format, update rules.

---

## 🌟 Intent

This Second Brain tracks your experience, education, and projects, acting as a single source of truth:
- **Master Resume**: Comprehensive database of all experience, projects, and skills to tailor from.
- **Interviews**: STAR stories, specs check.
- **Plan**: Track tasks, brainstorm ideas.

---

## 📁 Directory Structure

```text
Second Brain/
├── Employment/
│   ├── past.md           # Completed roles
│   ├── present.md        # Active roles & tasks
│   ├── future.md         # Career goals
│   ├── applied.md        # Job application tracker
│   ├── interview_prep.md # STAR PM stories
│   ├── references.md     # Reference list
│   ├── resume.html       # Master baseline resume
│   ├── resume.pdf        # Master baseline resume PDF (ignored)
│   ├── generate_pdf.py   # Playwright HTML→PDF compiler
│   └── tailored_resumes/
│       ├── *.html                  # Active tailored resumes (not yet archived)
│       ├── resume-pdfs/            # Compiled resume PDFs
│       ├── coverletter-pdfs/       # Compiled cover letter PDFs
│       ├── cover_letters/
│       │   ├── *.html              # Active cover letter HTMLs
│       │   └── *.txt               # Active cover letter plain texts
│       └── outreach/
│           └── *.txt               # Active outreach messages (.txt files)
├── Education/
│   ├── past.md           # Degrees/research
│   ├── present.md        # Active courses/certs
│   └── future.md         # Future topics
├── Projects/
│   ├── past.md           # Completed repos
│   ├── present.md        # Active dev
│   ├── future.md         # Backlog ideas
│   └── system_designs.md # Architecture notes
├── consume/              # Inbound docs (ignored)
│   └── jobs/             # Job specs (date-named .txt files)
├── archive/              # Processed docs (ignored)
│   ├── jobs/             # Archived job specs
│   └── tailored_resumes/
│       ├── *.html                  # Archived resume HTMLs
│       ├── resume-pdfs/            # Archived resume PDFs
│       ├── coverletter-pdfs/       # Archived cover letter PDFs
│       ├── cover_letters/
│       │   ├── *.html              # Archived cover letter HTMLs
│       │   └── *.txt               # Archived cover letter plain texts
│       └── outreach/
│           └── *.txt               # Archived outreach messages (.txt files)
├── skills_matrix.md      # Tech skills map
├── metrics_repository.md # Metrics DB
└── agents.md             # This file
```

---

## ✍️ Formatting Rules

1. **Time**: Group by Year (`# 2026`) and Month (`## May 2026`). Descending order (newest first).
2. **Impact**: Action verbs, bold key metrics, tech stacks. (e.g. *Optimized fees: **Python** simulation → **+30%** AOV*).
3. **Roles/Projects Layout**:
   - **Header**: Role/Company/Project + dates + links.
   - **Context**: One-sentence goal.
   - **Key Achievements**: Bullets by area (Feature, Optimization, Architecture, ML).
   - **Tech Stack**: Explicit list.
4. **Links**: Markdown style. Local files use relative links (e.g. `[Resume](./archive/Resume.pdf)`). Web links normal.
5. **Resume Chronology**: All resumes (baseline & tailored) must list professional experience in descending chronological order (newest first by end date; active roles marked "Present" at top). Never reorder blocks to match specs.

---

## 🔄 Agent Workflows

### 1. Retrieve
- **Resume**: Check `past.md` + [skills_matrix.md](./skills_matrix.md) + [metrics_repository.md](./metrics_repository.md).
- **Interview**: Check [interview_prep.md](./Employment/interview_prep.md) + [system_designs.md](./Projects/system_designs.md).

### 2. Update
When task/role ends or new experiences/projects are added:
1. **Move**: For completed roles/tasks, move `present.md` → `past.md` under current month/year. Update dates.
2. **Skills**: Add new tech to [skills_matrix.md](./skills_matrix.md).
3. **Metrics**: Append results to [metrics_repository.md](./metrics_repository.md).
4. **STAR**: Add story to [interview_prep.md](./Employment/interview_prep.md).
5. **Design**: Document architecture in [system_designs.md](./Projects/system_designs.md).
6. **Master Resume**: Sync all new experiences, achievements, education details, and projects directly to the master [resume.html](./Employment/resume.html) to keep it fully comprehensive.

### 3. Consume
When files added to [consume/](./consume/):
1. **Parse**: Extract achievements, metrics, designs.
2. **Update**: Distribute edits to past, present, skills, metrics, and sync all new content into the master [resume.html](./Employment/resume.html).
3. **Confirm**: Ask user for approval.
4. **Archive**: Move to [archive/](./archive/).

### 4. Job Applications

Triggered when job specs are present in [consume/jobs/](./consume/jobs/).

**For each job spec, complete all steps below before moving on to the next:**

#### Step 1 — Tailor Resume
- Read `Employment/past.md` and `Employment/present.md` to source experience bullets.
- Copy the master `Employment/resume.html` as the base. Do not start from scratch.
- Prune and tailor bullets to fit on **exactly 1 page** — prioritize the experience and projects most relevant to the job spec.
- Maintain the exact same HTML layout, CSS, and style as the master resume.
- Keep professional experience in descending chronological order (newest first). Never reorder blocks.
- Save as: `tailored_resumes/resume_[Company]_[RoleCode]_[Month]_[Year].html`
  - Example: `resume_Orbital_PM_June_2026.html`

#### Step 2 — Write Cover Letter
- Follow the **Cover Letter Guide** below.
- Address to a named recruiter if one is identified in the job spec; otherwise use "Hiring Team / [Company]".
- Save as: `tailored_resumes/cover_letters/cover_letter_[Company]_[RoleCode]_[Month]_[Year].html`
  - Example: `cover_letter_Orbital_PM_June_2026.html`

#### Step 2.5 — Write Outreach Message
- Follow the **Outreach Message Guide** below.
- Save as a plain text file: `tailored_resumes/outreach/outreach_[Company]_[RoleCode]_[Month]_[Year].txt`
  - Example: `outreach_Orbital_PM_June_2026.txt`

#### Step 3 — Compile PDFs
Run the PDF generation script from the `Employment/` directory. **Always use the miniconda Python interpreter** (or your local python environment with Playwright configured).

```bash
cd Employment && python3 generate_pdf.py
```

The script auto-discovers all HTML files and writes:
- Resume PDFs → `tailored_resumes/resume-pdfs/`
- Cover letter PDFs → `tailored_resumes/coverletter-pdfs/`

Each PDF is auto-scaled to fit exactly 1 page.

#### Step 4 — Confirm with User
Present a summary of what was created (company, resume path, cover letter path, outreach path, PDF paths). Ask the user to review before proceeding.

Do not log or archive anything yet.

#### Step 5 — Log to Tracker (On Apply Confirmation Only)
**Wait for explicit user confirmation that they have applied before doing this step.**

Append a new row to the `Employment/applied.md` table under the correct Year/Month heading. Use this exact format:

```markdown
| **[Company]** | [Full Role Title] | [Month Day, Year] | Applied | [Resume HTML](../archive/tailored_resumes/resume_[slug].html) • [Resume PDF](../archive/tailored_resumes/resume-pdfs/resume_[slug].pdf)<br>[Cover Letter HTML](../archive/tailored_resumes/cover_letters/cover_letter_[slug].html) • [Cover Letter PDF](../archive/tailored_resumes/coverletter-pdfs/cover_letter_[slug].pdf) • [Cover Letter TXT](../archive/tailored_resumes/cover_letters/cover_letter_[slug].txt)<br>[Outreach Message](../archive/tailored_resumes/outreach/outreach_[slug].txt) |
```

Note: links point to the **archive** paths (where they will be after step 6), not the current `tailored_resumes/` paths.

Also increment the summary count at the top of `applied.md` (e.g. `**June 2026**: 35 applications` → `36`).

#### Step 6 — Archive (On Apply Confirmation Only)
**Only after step 5 is complete**, move all files for the confirmed applications:

```bash
# Resumes
mv "tailored_resumes/resume_[slug].html" "../../archive/tailored_resumes/"
mv "tailored_resumes/resume-pdfs/resume_[slug].pdf" "../../archive/tailored_resumes/resume-pdfs/"

# Cover letters
mv "tailored_resumes/cover_letters/cover_letter_[slug].html" "../../archive/tailored_resumes/cover_letters/"
mv "tailored_resumes/coverletter-pdfs/cover_letter_[slug].pdf" "../../archive/tailored_resumes/coverletter-pdfs/"
mv "tailored_resumes/cover_letters/cover_letter_[slug].txt" "../../archive/tailored_resumes/cover_letters/"

# Outreach messages
mv "tailored_resumes/outreach/outreach_[slug].txt" "../../archive/tailored_resumes/outreach/"

# Job spec
mv "../../consume/jobs/[date].txt" "../../archive/jobs/"
```

The job spec file is only archived once all jobs in that file have been confirmed applied.

---

#### Application Q&A

When the user asks questions about an application, interview prep, or prompts related to a job — answer in natural, continuous prose. No bullet points, no dash lists, no bolded list headers. Write as a human would write, in conversational paragraphs.

---

## 📝 Cover Letter Guide

A cover letter is a marketing document. Keep to 1 A4 page. Sell the candidate — no storytelling for its own sake.

### Formatting Rules
- **Style**: Times New Roman 11pt, clean layout — match the resume header exactly (name, contact info, date, recipient block).
- **Length**: 1 A4 page. 5–6 paragraphs maximum.
- **Tone**: Natural, human, confident prose. No bullet points, no dash lists (`-`), no numbered lists, no bolded paragraph headers anywhere in the letter body.
- **Save**: HTML first, then compile to PDF via `generate_pdf.py`. Also produce a plain `.txt` version in the `cover_letters/` directory.

---

### Step 1: Parse the Job Spec

1. Read the responsibilities section. Identify the top 2–3 bullets that match past work most directly.
2. Read the qualifications. Identify met requirements and nice-to-haves.
3. Select **two** qualifications to anchor the match paragraphs.
4. Note the company name, recruiter name (if present), and any named products, partners, or recent news.

---

### Step 2: Research Company Fit

Identify two reasons for fit:
1. **Value/mission reason** — principles, culture, or problem domain that resonates.
2. **Topical reason** — funding round, product launch, named partnership, blog post, or market timing.

Connect both to the candidate's goals.

---

### Step 3: Write the Letter

**Header**
- Name, contact info (matching resume header)
- Date (full: e.g. "22 June 2026")
- Recipient: Named recruiter + title + company if known; otherwise "Hiring Team / [Company]"

**Paragraph 1 — Intro** (2 sentences max)
- State the role being applied for.
- Lead with one strong differentiating claim + one specific company detail that signals genuine interest.

**Paragraph 2 — 12-Month Transition**
- Summarize the past 12 months: 3–4 achievements with metrics and tech, high specificity, no jargon.
- End with: "I am excited to contribute at [Company]. Three reasons make me a strong fit."

**Paragraph 3 — First Match (Experience Theme)**
- Opening sentence states the career theme (e.g. "The defining theme of my product work is…").
- Connect the theme to the first selected qualification.
- One specific story from experience, backed by a bold metric.
- Themes to draw from: *Leading People, Taking Initiative, Challenge Affinity, Specific Work Affinity, Technical Depth, Cross-functional Complexity, Failure Management, Curiosity Driven*.

**Paragraph 4 — Second Match (Experience Theme)**
- Same structure: theme → qualification → story + metric.
- Use a different theme and a different role/experience than paragraph 3.

**Paragraph 5 — Company Fit**
- Open with: "Third, I follow [Company] closely."
- Weave the value reason and topical reason together.
- Connect both to what makes this role exciting at this specific moment for the company.

**Paragraph 6 — Closing** (2 sentences)
- Terse. "I would welcome the chance to discuss the role. Thank you for your time."
- Sign off: "Sincerely, [Name]"

---

## ✉️ Outreach Message Guide

Outreach messages must follow the high-impact "tldr-driven" cold email format to maximize response rates. Keep it concise, direct, and focused on execution over strategy.

### Formatting Rules
- **Subject**: Use standard patterns like `RE: [Role Title] at [Company]`.
- **tldr; Block**: Place a `tldr;` section at the very top. Keep it punchy, honest, and execution-oriented (e.g., stating a preference for shipping features over strategy decks, and detailing your specific focus).
- **Paragraph 1 — Credibility**: Briefly state interest in the role and establish background credibility by listing 5 years of experience at previous companies with links to their websites.
- **Paragraph 2 — Core Value Proposition**: Focus on the specific system implementations and metrics relevant to the target role (e.g., ML personalization engines driving metrics, compliance pipelines, cohort tracking).
- **Paragraph 3 — Relocation & Close**: Express interest in joining the team, specify relocation/location details if relevant, and ask for a 15-minute chat.
- **Sign off**: Use a brief closure and include links to your contact info, LinkedIn, and GitHub.

---

## 🔖 Quick Reference

| Task | Command / Path |
|---|---|
| Generate PDFs | `cd Employment && python3 generate_pdf.py` |
| Resume HTML output | `Employment/tailored_resumes/resume_[slug].html` |
| Resume PDF output | `Employment/tailored_resumes/resume-pdfs/resume_[slug].pdf` |
| Cover letter HTML output | `Employment/tailored_resumes/cover_letters/cover_letter_[slug].html` |
| Cover letter PDF output | `Employment/tailored_resumes/coverletter-pdfs/cover_letter_[slug].pdf` |
| Cover letter TXT output | `Employment/tailored_resumes/cover_letters/cover_letter_[slug].txt` |
| Outreach message output | `Employment/tailored_resumes/outreach/outreach_[slug].txt` |
| Archive resume HTML | `archive/tailored_resumes/resume_[slug].html` |
| Archive resume PDF | `archive/tailored_resumes/resume-pdfs/resume_[slug].pdf` |
| Archive cover letter HTML | `archive/tailored_resumes/cover_letters/cover_letter_[slug].html` |
| Archive cover letter PDF | `archive/tailored_resumes/coverletter-pdfs/cover_letter_[slug].pdf` |
| Archive cover letter TXT | `archive/tailored_resumes/cover_letters/cover_letter_[slug].txt` |
| Archive outreach message | `archive/tailored_resumes/outreach/outreach_[slug].txt` |
| Archive job spec | `archive/jobs/[date].txt` |
| Application tracker | `Employment/applied.md` |
