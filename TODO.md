# CV Improvement Plan

A checklist for getting the CV and site ready for tech job applications.
Tick items off (`- [ ]` → `- [x]`) as you go. Items are roughly in order of impact.

**How to work from this list:** for each chunk of work, make a branch
(`git switch -c projects-section`), commit your changes there, push it, and open
a Pull Request into `main`. That gives you a preview of the diff, a place for
feedback, and a clean history. Merging into `main` still triggers the PDF rebuild
as before.

---

## 1. Projects (biggest impact)

- [ ] Point each project link at its **own repo**, not the GitHub profile page
- [ ] Give each project repo a README: what it does, how to run it, a screenshot or sample output
- [ ] Build one **original** project that uses the horticulture background. Idea:
  - A Go service that ingests hydroponic sensor readings (EC, pH, temp, humidity)
  - Stores them in PostgreSQL, exposes a REST API, flags readings that drift out of range
  - Runs in Docker, has tests, and has a short README with an architecture diagram
- [ ] Once there's an original project, lead with it; consider dropping Bookbot or Asteroids (both standard Boot.dev course projects)

## 2. Positioning & summary

- [x] Pick a headline aimed at tech roles, e.g. *"Backend Developer (Go / Python) with an agtech background"*
- [x] Rewrite **About Me** in 2–3 sentences: what you build, with what, and what role you want.
      Cut generic phrases ("dedicated and adaptable", "proven ability to…")
- [x] Update the `<title>` and meta description to match the new headline

## 3. Experience

- [ ] Expand the Square Mile Farms "automated sensing" bullet into the specifics: what did you automate or measure, with what tools, and what changed?
- [ ] Add numbers wherever they're true (crops managed, batches per week, yield change, etc.)
- [ ] Trim non-tech roles to one bullet each about transferable skills

## 4. Skills & education

- [ ] Replace weak entries ("HTML5 / CSS3", "Docker fundamentals") with concrete skills actually used: HTTP servers, REST APIs, PostgreSQL, testing, auth…
- [ ] Boot.dev: state completed status, list the main courses, link to the certificate or profile

## 5. Presentation & technical polish

- [ ] Check the PDFs parse cleanly for applicant tracking systems (copy-paste the text out of `CV.pdf` — does it come out in a sensible order?)
- [ ] Confirm the web fonts render in the generated PDFs (not fallback fonts)
- [ ] Add Open Graph tags and a favicon so links shared on LinkedIn show a proper preview
- [ ] Add a small "Source" link to this repo; the auto-generated PDFs are a nice detail
- [ ] Make the LinkedIn link text match the real URL
- [ ] Remove "References are available upon request"

## 6. GitHub profile

- [ ] Pin the best 3–4 repos
- [ ] Add a short profile README (who you are, what you're building, what you're looking for)

## 7. Later: tailored versions

- [ ] Consider generating role-specific CV variants (general backend vs agtech-focused) from the same source, like the existing 1-page / 2-page split
