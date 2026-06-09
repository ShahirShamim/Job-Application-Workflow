# 🤖 AI Agent Setup Guide: Initialize Second Brain

This file instructs AI agents on how to initialize this directory structure with a user's professional data. If you are an AI assistant (Claude, Gemini, ChatGPT, etc.) helping a user set up this repo, follow these instructions step-by-step.

---

## 📋 Initialization Workflow

### Step 1: Request the User's Resume
Ask the user to provide their current resume or CV. They can:
- Copy-paste the text of their resume into the chat.
- Provide a path to a local file (PDF, TXT, HTML) if you have access to read it.
- Paste the content of their LinkedIn profile.

### Step 2: Parse and Extract Data
Analyze the provided resume and extract the following:
1. **Contact Info**: Full name, headline, phone number, email, location, LinkedIn, and GitHub links.
2. **Summary**: A concise paragraph detailing years of experience and core strengths.
3. **Core Competencies**: List of skills grouped by product/methodologies, languages/frameworks, and tools.
4. **Professional Experience**: Companies, locations, roles, start/end dates, achievements, and metrics.
5. **Projects**: Repository names, dates, contexts, and technologies used.
6. **Education**: Universities, locations, degrees, honors, specializations, and coursework.

### Step 3: Populate Files
Distribute the extracted information into the repository templates. Ensure you strictly follow the **Formatting Rules** in [agents.md](./agents.md) (newest first, group by Year `# 2026` and Month `## June 2026`, use bold metrics).

Write the content to the following files:

#### 1. Master HTML Resume: `Employment/resume.html`
- Update the `<title>`, `<h1>` header, headline, contact information, summary, and core competencies.
- Replace the placeholder `.job-block` elements with their actual professional history.
- Ensure all achievements use `<strong>[Achievement Area]:</strong>` and wrap key metrics (percentages, speedups, valuations) in `<span class="bold-metric">...</span>`.
- Populate Projects and Education sections matching the exact HTML structure and CSS classes.

#### 2. Employment History: `Employment/present.md` & `Employment/past.md`
- Move any *active* role to [present.md](./Employment/present.md).
- Move all *previous* roles to [past.md](./Employment/past.md) in descending chronological order.
- Format achievements into bullet lists by area (e.g., Feature, Optimization, Architecture, ML).

#### 3. Education: `Education/present.md` & `Education/past.md`
- Populate degrees, honors, and coursework in [past.md](./Education/past.md).
- Put active courses, self-study topics, or pending certifications in [present.md](./Education/present.md).

#### 4. Projects: `Projects/present.md` & `Projects/past.md`
- Populate any active projects in [present.md](./Projects/present.md).
- Populate completed repositories and side projects in [past.md](./Projects/past.md).

#### 5. Skills & Metrics Databases
- Populate [skills_matrix.md](./skills_matrix.md) mapping their skills to where they were applied.
- Scan their achievements for numbers (dollars, percentages, time savings) and populate [metrics_repository.md](./metrics_repository.md).

#### 6. Support Files
- **applied.md**: Leave this empty but ensure the structure is intact.
- **references.md**: Populate with tables for their past companies, setting placeholders like `[Manager Name]`, `[Email]` so the user can easily fill them in.
- **interview_prep.md**: Draft 1 or 2 STAR story skeletons based on their most prominent achievements.

### Step 4: Verify and Build
1. Check that all files are updated and contain no raw template tags (e.g. `[Your Name]`).
2. Run `generate_pdf.py` to verify that the master HTML resume compiles successfully into a PDF:
   ```bash
   python Employment/generate_pdf.py
   ```
3. Inform the user that setup is complete and provide a summary of the imported roles.
