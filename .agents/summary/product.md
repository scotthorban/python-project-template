# Product Summary

## Purpose

`python-project-template` is a **GitHub repository template** that provides a fully configured, opinionated Python
project scaffold. Its goal is to eliminate setup friction — a developer can clone this template and begin writing domain
logic immediately, with all tooling wired up and enforced from day one.

## Key Business Objectives

1. **Reduce project bootstrap time** — all toolchain config is pre-populated and tested.
2. **Enforce consistency** — shared linting, formatting, type-checking, and commit message conventions across all
   projects derived from this template.
3. **Automate quality gates** — tests, coverage (≥ 80 %), lint, format, type checks, and badge generation run
   automatically on every push/PR via GitHub Actions.
4. **Automated releases** — merging to `main` triggers a git tag and GitHub Release derived from `pyproject.toml`
   `version`, with auto-generated release notes.
5. **Security baseline** — `detect-secrets` scans prevent accidental credential commits at both pre-commit and CI
   stages.

## Target Users

- Python developers who want a consistent, standardised starting point for their python projects.
- Engineers creating new internal Python packages that depend on the private `common-py` library.
- Teams who want CI/CD, badge reporting, and release automation out of the box.

## Notable Constraints

- Depends on the **private** `common-py` library via SSH git (`ssh://git@github.com/scotthorban/common-py.git`). The CI
  workflow requires a `COMMON_PY_READ_KEY` GitHub secret.
- Python ≥ 3.11.8 is required.
- The template is intentionally minimal in `src/` — the stub `run_project.py` and its test are placeholders that
  consumers replace with real logic.
