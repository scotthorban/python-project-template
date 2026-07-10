# Structure Summary

## Directory Tree

```
python-project-template/
├── .agents/                        # AI agent steering files
│   ├── skills/                     # Custom agent skills
│   └── summary/                    # This directory — high-level summaries
│       ├── product.md
│       ├── tech.md
│       └── structure.md
├── .github/
│   ├── pull_request_template.md    # PR template
│   └── workflows/
│       ├── test.yml                # CI: run tests + update badges
│       └── tag_and_release.yml     # CD: tag + GitHub Release on main
├── docs/
│   └── img/                        # Generated badge SVGs (committed to repo)
├── reports/                        # Test/lint output artifacts (gitignored typically)
│   ├── unit-tests.xml
│   ├── coverage.xml
│   ├── ruff.json
│   └── ty.json
├── src/                            # Application source package
│   ├── __init__.py
│   └── run_project.py              # Entry point (placeholder — replace with real logic)
├── tests/
│   ├── __init__.py
│   ├── unit/                       # Unit tests
│   │   ├── __init__.py
│   │   └── test_run_project.py
│   └── functional/                 # Functional/integration tests
│       ├── __init__.py
│       └── test_functional.py
├── .coveragerc                     # Coverage exclusions and report config
├── .gitattributes                  # Git line-ending and diff attributes
├── .gitignore                      # Python ecosystem ignores
├── .pre-commit-config.yaml         # Pre-commit hook definitions
├── .secrets.baseline.json          # detect-secrets scanned baseline
├── AGENTS.md                       # AI agent steering (ASDLC)
├── CHANGELOG.md                    # Semantic version history
├── README.md                       # Developer documentation
├── definitions.py                  # Project-level constants (PROJECT_ROOT_DIR)
├── pyproject.toml                  # Single source of truth for all tool config
└── uv.lock                         # Reproducible dependency lock file
```

## Layer Separation

| Layer              | Location                                                   | Responsibility                                                              |
|--------------------|------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Source**         | `src/`                                                     | Application / library logic only. No test code, no config.                  |
| **Tests**          | `tests/unit/`, `tests/functional/`                         | Unit tests isolated from functional/integration tests.                      |
| **Config**         | `pyproject.toml`, `.coveragerc`, `.pre-commit-config.yaml` | All tooling config centralised; avoid per-tool config files where possible. |
| **CI/CD**          | `.github/workflows/`                                       | Automation only; no business logic.                                         |
| **Docs / Badges**  | `docs/img/`                                                | Generated artefacts committed back to the repo by CI.                       |
| **Reports**        | `reports/`                                                 | Machine-readable test/lint outputs consumed by badge generator.             |
| **Agent Steering** | `.agents/`, `AGENTS.md`                                    | AI coding guidance; not deployed or tested.                                 |

## Naming Conventions

- **Source files**: `snake_case.py`
- **Test files**: `test_<module_name>.py` or `test_<concern>.py`
- **Test classes**: `Test<Subject>` (inheriting `unittest.TestCase` for unit tests; plain class for functional)
- **Test methods**: `test_<behaviour>()`
- **Constants**: `UPPER_SNAKE_CASE` (see `definitions.py`, `test_functional.py`)
- **Workflow files**: `snake_case.yml`
- **Versions**: Semantic versioning in `pyproject.toml`; git tags prefixed `v` (e.g. `v2.4.3`)
- **Commit messages**: Conventional Commits format (enforced by `conventional-pre-commit` hook)

## Key Constraints

- `definitions.py` at the root provides `PROJECT_ROOT_DIR` as a `Path` object — import from here rather than computing
  `__file__` paths ad-hoc.
- `src/` is an implicit namespace package installed in editable mode by `uv`; tests import
  `from src.<module> import ...`.
- Coverage excludes `__init__.py`, `tests/*`, and `definitions.py` (see `.coveragerc`).
- The `reports/` directory must exist for CI task outputs; the badge task reads from it.
