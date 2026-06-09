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
│   └── tailored_resumes/ # Tailored resumes
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
│   └── jobs/             # Job specs
├── archive/              # Processed docs (ignored)
│   ├── Resume.pdf        # Master resume archive (PDF)
│   ├── resume_b.html
│   ├── jobs/             # Past job specs
│   └── tailored_resumes/ # Archived tailored resumes & cover letters
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
When job spec added to [consume/jobs/](./consume/jobs/):
1. **Analyze**: Parse job requirements.
2. **Match**: Retrieve matching experience bullets and qualifications from [past.md](./Employment/past.md) and [present.md](./Employment/present.md).
3. **Tailor**: Use the **Job Applier Workflow** skill to optimize bullets. Copy the master [resume.html](./Employment/resume.html) to [tailored_resumes/](./Employment/tailored_resumes/). Modify and prune bullets to fit on 1 page (leveraging the master resume as the comprehensive source of truth). Maintain layout/style exactly. Name format: `resume_[Company]_[Role]_[Month]_[Year].html`.
4. **Cover Letter**: Write tailored cover letter using the Cover Letter Guide. Save as HTML name format: `cover_letter_[Company]_[Role]_[Month]_[Year].html` inside `tailored_resumes/cover_letters/`.
5. **Compile PDF**: Run [generate_pdf.py](./Employment/generate_pdf.py) on the created/modified HTML resume and cover letter to produce or update matching PDFs in `tailored_resumes/PDFs/` and `tailored_resumes/cover_letters/PDFs/`.
6. **Confirm**: Ask user review.
7. **Tracker**: Append job to [applied.md](./Employment/applied.md). List company, role, date, status. Link to their future archive paths (under `archive/tailored_resumes/`).
8. **Archive (On Apply)**: DO NOT move the HTML and PDF resumes/cover letters from `tailored_resumes/` to the `archive/` folder, and DO NOT move the job spec from `consume/jobs/` to `archive/jobs/` until the user explicitly confirms they have applied. Once confirmed:
   - Move HTML and PDF resumes/cover letters from `tailored_resumes/` to `archive/tailored_resumes/` (preserving subfolder structure).
   - Move job spec from `consume/jobs/` to `archive/jobs/`.
9. **User Questions**: If the user asks any questions related to the application, writing prompts, or interview questions after consuming a job, answer in text that feels genuinely human-written. Do not use bullet points, dash lists (`-`), bolded list headers, or other common robotic/AI traits. Write in natural, continuous, and conversational paragraphs.

---

## 📝 Cover Letter Guide

Cover letter marketing tool. No story book. Keep 1 A4 page. Sell self.

### Step 1: Parse Job Spec

1. Read "What you do". Highlight top bullets matching past work.
2. Read "Qualifications". Highlight met requirements and nice-to-haves.
3. Make two-column table. Left: job requirements. Right: matching experience. Use exact terms from spec (speak employer language).
4. Select top two qualifications.

### Step 2: Research Company

Find two reasons for fit:
1. Value-driven reason (principles, culture, mission).
2. Topical reason (news, product launch, funding, blog post).
Connect both to personal goals.

### Step 3: Write Cover Letter Structure

1. **Header**: Personal contact info, date, recipient details.
2. **Intro** (1-2 sentences): State target role, intent, belief. Highlight key strength. Mention specific company detail.
3. **Transition**:
   - Write summary statement: achievements, metrics, tech from past year. No jargon, high specificity.
   - Flow sentence: "Over past 12 months, I [metrics]. Excited to contribute at [Company]. Three reasons make me perfect fit:"
4. **Match Body** (2 paragraphs):
   - Map each qualification to theme. Themes: *Leading People, Taking Initiative, Challenge Affinity, Different Work Affinity, Specific Work Affinity, Failure Management, Conflict Management, Curiosity Driven*.
   - Paragraph structure:
     - Sentence 1 (Theme): "Theme defining career is [theme]."
     - Sentence 2 (Qualification): Connect theme to qualification.
     - Sentence 3 (Story): Detail specific story, back with bold metrics.
5. **Company Fit** (1 paragraph):
   - Weave value reason and topical reason.
   - Template: "Third, follow [Company] closely. Resonate with values and direction. [Value] stands out because [Reason]. Also read [Topical Reason] which appeals because [Why]."
6. **Conclusion**:
   - Terse closing: "Experience fits [Company] and [Role]. Ready to level up skills with team. Look forward to hearing back. Sincerely, [Name]."

### Formatting

Match resume style (Times New Roman, 11pt, clean layout). Save HTML, compile PDF.

