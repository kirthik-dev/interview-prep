# Kirthik’s Field Notes

A buildless, accessible interview study guide for resume explanations, three personal data projects, data engineering, production scenarios, forecasting, MLOps and RAG.

- **97 Q&A in 16 chapters**, 24 generic code examples and 58 glossary entries.
- Static HTML/CSS and vanilla JavaScript; no CDN, external font, package install, analytics, login or backend.
- Search across answers, native collapsible questions, expand/collapse, code copying, deep links, print/save PDF.
- Core content works without JavaScript. Small code examples show their prerequisites and expected outcomes.
- Resume/repository facts, user-described work, proposed designs and hypothetical practice are labeled. Contact details and credentials are excluded.

## Preview

```sh
python3 -m http.server 8765
```

Open http://127.0.0.1:8765/ from this directory.

## Update content

Edit `tools/content.py`, then regenerate and verify:

```sh
python3 tools/build.py
python3 tools/verify.py
node --check app.js
node tools/check-print.cjs
```

Python uses only the standard library. The checked-in `index.html` is the served artifact; no build runs on GitHub Pages.

## Publish on GitHub Pages

The intended repository is `kirthik-dev/interview-prep`, publishing the root of `main`. The `.nojekyll` file disables Jekyll processing.

The deployment helper `python3 tools/publish.py` requests a token using hidden input and never saves it. It verifies the account, waits for `PUBLISH`, and creates a **new** public repository; it refuses to overwrite an existing repository. It uses GitHub’s REST API to create one content commit and enable branch-based Pages. It needs repository creation/content/Pages permissions. For future edits to an existing repository, use normal Git with your own authenticated setup, then Pages rebuilds from `main`.

The expected site address is https://kirthik-dev.github.io/interview-prep/ (valid only after successful deployment).

## Coverage and evidence

See [coverage checklist](docs/coverage.md), [question manifest](docs/content-manifest.json), and the sources section on the page. Software feature support varies by release. This study guide does not recover unavailable private employer code or invent historical model metrics.
