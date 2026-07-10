# Technology Summary

## Language

- **Python** ≥ 3.11.8 (target: `py311`)

## Package & Project Management

| Tool      | Version Constraint | Role                                             |
|-----------|--------------------|--------------------------------------------------|
| `uv`      | ≥ 0.11.26          | Package manager, virtualenv, task runner wrapper |
| `uv.lock` | —                  | Lock file for reproducible installs              |

## Runtime Dependencies

| Package            | Source                     | Notes                    |
|--------------------|----------------------------|--------------------------|
| `common-py[utils]` | Private SSH git (`v0.5.1`) | Internal utility library |

## Development Dependencies

| Package             | Version  | Role                                    |
|---------------------|----------|-----------------------------------------|
| `ruff`              | ≥ 0.15.0 | Linting and formatting                  |
| `ty`                | ≥ 0.0.56 | Static type checking                    |
| `pytest`            | ≥ 8.4.1  | Test runner                             |
| `pytest-cov`        | ≥ 6.2.1  | Test coverage reporting                 |
| `taskipy`           | ≥ 1.14.1 | Task runner (wraps common dev commands) |
| `detect-secrets`    | ≥ 1.5.0  | Secret scanning                         |
| `prek`              | ≥ 0.4.8  | Pre-commit hook manager                 |
| `typing-extensions` | ≥ 4.14.1 | Backported typing utilities             |

## Linting & Formatting Rules

- `ruff` configured in `pyproject.toml`:
    - Rule set: `ALL` (with selective ignores: `COM812`, `D100`, `D104`)
    - `S101` (assert detection) disabled for test files
    - Docstring convention: **Google**
    - Line length: **120**
    - Import sort: case-sensitive, combine-as-imports
    - Quote style: `double`, indent: `space`

## Testing

- **Framework**: `pytest`
- **Coverage**: `pytest-cov`, minimum threshold **80 %**, configured in `.coveragerc`
- **Output**: JUnit XML (`reports/unit-tests.xml`), coverage XML (`reports/coverage.xml`)

## Pre-commit Hooks (via `prek`)

Configured in `.pre-commit-config.yaml`:

| Hook                            | Version | Stage        |
|---------------------------------|---------|--------------|
| `conventional-pre-commit`       | v3.2.0  | `commit-msg` |
| `check-yaml` (pre-commit-hooks) | v2.3.0  | pre-commit   |
| `detect-secrets`                | v1.5.0  | pre-commit   |
| `ruff` (linter, `--fix`)        | v0.15.0 | pre-commit   |
| `ruff-format`                   | v0.15.0 | pre-commit   |

## Task Runner (taskipy)

Invoked as `uv run task <name>`:

| Task                  | Command Summary                                          |
|-----------------------|----------------------------------------------------------|
| `install-hooks`       | Install pre-commit and commit-msg hooks                  |
| `detect-secrets-scan` | Update secrets baseline                                  |
| `audit-secrets`       | Manually review detected secrets                         |
| `unit`                | Run unit + functional tests, output JUnit XML            |
| `coverage`            | Run coverage (≥ 80 %)                                    |
| `check-lint`          | Run ruff linter (also outputs JSON report)               |
| `lint`                | Run ruff linter with auto-fix                            |
| `check-format`        | Show ruff formatting diff                                |
| `format`              | Apply ruff formatting                                    |
| `check-types`         | Run `ty` type checker (also outputs GitLab JSON)         |
| `badge`               | Generate SVG badges from report files                    |
| `tests`               | Run all: unit → coverage → lint → format → types → badge |

## CI/CD (GitHub Actions)

| Workflow              | Trigger                             | Purpose                                            |
|-----------------------|-------------------------------------|----------------------------------------------------|
| `test.yml`            | Push to `main`, any PR, manual      | Run `uv run task tests`, commit updated badges     |
| `tag_and_release.yml` | After `test.yml` succeeds on `main` | Tag + GitHub Release from `pyproject.toml` version |

**Required GitHub Secrets:**

- `PAT` — Personal access token for checkout + badge commit
- `COMMON_PY_READ_KEY` — SSH private key for accessing the private `common-py` dependency
- `GITHUB_TOKEN` — Built-in token for pushing tags

## Badge Generation

`generate-badges` (provided by `common-py`) reads report files and writes SVGs to `docs/img/`:

- `python.svg`, `unittest.svg`, `coverage.svg`, `ruff.svg`, `ty.svg`, `release.svg`
