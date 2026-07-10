# AGENTS.md

> AI agent steering file following the [ASDLC open standard](https://asdlc.dev).  
> Keep this file updated as the project evolves.

---

## Mission

A reusable Python project template providing a production-ready scaffolding for new Python packages. It encodes
opinionated defaults for package management (`uv`), linting/formatting (`ruff`), type-checking (`ty`), testing (
`pytest`), secret scanning (`detect-secrets`), pre-commit hooks (`prek`), CI (`GitHub Actions`), and automated badge
generation — so engineers can clone and build immediately without toolchain setup.

---

## Toolchain Registry

| Concern                      | Tool                                       | Config Location                         |
|------------------------------|--------------------------------------------|-----------------------------------------|
| Package / project management | `uv`                                       | `pyproject.toml`, `uv.lock`             |
| Linting                      | `ruff check`                               | `pyproject.toml [tool.ruff]`            |
| Formatting                   | `ruff format`                              | `pyproject.toml [tool.ruff.format]`     |
| Type checking                | `ty`                                       | `pyproject.toml` (taskipy task)         |
| Testing                      | `pytest`                                   | `pyproject.toml` (taskipy task)         |
| Test coverage                | `pytest-cov`                               | `.coveragerc`, 80 % minimum             |
| Secret scanning              | `detect-secrets`                           | `.secrets.baseline.json`                |
| Pre-commit hooks             | `prek`                                     | `.pre-commit-config.yaml`               |
| Task runner                  | `taskipy`                                  | `pyproject.toml [tool.taskipy.tasks]`   |
| Badge generation             | `generate-badges` (via `common-py`)        | taskipy `badge` task                    |
| CI pipeline                  | GitHub Actions                             | `.github/workflows/test.yml`            |
| Release automation           | GitHub Actions + `ncipollo/release-action` | `.github/workflows/tag_and_release.yml` |
| Internal library             | `common-py[utils]` (private SSH git dep)   | `pyproject.toml [tool.uv.sources]`      |

**Run all checks in one command:**

```shell
uv run task tests
```

---

## Judgment Boundaries

### ✅ Agents MAY

- Add new source modules under `src/`.
- Add unit tests under `tests/unit/` and functional tests under `tests/functional/`.
- Update `pyproject.toml` dependencies and taskipy tasks.
- Extend `.pre-commit-config.yaml` with new hooks.
- Modify `CHANGELOG.md` and `README.md`.
- Update badge SVGs under `docs/img/`.

### ⚠️ Agents MUST check with the user before

- Changing the `version` field in `pyproject.toml` (triggers a GitHub Release when merged to `main`).
- Altering the SSH deploy key handling in `.github/workflows/test.yml` (accesses the private `common-py` dependency).
- Modifying the `tag_and_release.yml` workflow (controls production release cadence).
- Changing the `requires-python` constraint (may break downstream users of the template).

### 🚫 Agents MUST NOT

- Commit secrets or credentials to any file (enforced by `detect-secrets`).
- Lower the coverage threshold below 80 % in `.coveragerc` / taskipy `coverage` task.
- Switch the package manager away from `uv` without explicit user instruction.
- Disable or bypass ruff lint rules globally without user approval.
