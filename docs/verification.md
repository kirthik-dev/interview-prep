# Verification record

## Passed before publication

- Generated static HTML contains 97 complete question/answer lessons in 16 chapters, 24 code examples, 58 glossary entries and direct links to all three repositories.
- Every lesson includes a plain explanation, example, short answer, detailed answer, follow-up and common mistake.
- All 168 HTML IDs are unique; internal anchors and local asset/document paths resolve.
- JavaScript syntax check passed.
- Eight dependency-free Python teaching examples were executed and matched their documented results. Spark, dbt, SQL, FastAPI and MLflow examples were syntax/review checked where applicable; their external environments were not provisioned or executed.
- Credential/contact-pattern scan passed for all publishable files, including tools. No user credential is saved to the project.
- In-app browser: search filters and opens matches; clearing restores all 97; empty search shows a message; expand/collapse follows the current result set.
- In-app browser: all 24 Copy code buttons wrote exactly the expected snippets to the clipboard; keyboard Tab reaches Expand all from Search and Enter expands a question. All 18 navigation links reached the correct visible sections. Navigation out of filtered results clears the filter.
- Desktop visual inspection passed. Mobile inspected at 320 × 740 and 390 × 844; no document-level horizontal overflow. Tables/code have their own horizontal scrolling.
- Print-state test passed: beforeprint opens all 97 lessons and removes search hiding; afterprint restores the previous state, including repeated print events.

## Verification limit

The in-app browser’s operating-system print dialog blocked automation when invoked. It did not expose a preview for visual inspection. Print CSS and state transitions were checked, but a rendered print/PDF pagination review was not completed. No claim of perfect print layout is made.

## Deployment

The delivery message reports the actual repository, Pages build and live-site verification result. The expected address alone is not proof of deployment.

## Live deployment verified

- Source: https://github.com/kirthik-dev/interview-prep
- Site: https://kirthik-dev.github.io/interview-prep/
- GitHub Pages reported the source build as `built` with no error.
- Live HTML, CSS, JavaScript, favicon, coverage checklist and question manifest each returned HTTP 200 and matched their local source bytes exactly.
- Live in-app browser: all 97 answers present, stylesheet loaded and no document horizontal overflow.
- Live search for MLflow returned 10 answers; collapse produced zero visible open answers and expand reopened all 10.
- Live MLflow example copy matched the source snippet exactly.
- Live project navigation cleared the filter and reached Healthcare; a direct SCD2 answer URL opened the intended question.
- No browser errors or warnings were recorded during the live checks.

These checks establish the tested behavior. They do not establish that every external platform example was executed or that native print pagination is perfect.
