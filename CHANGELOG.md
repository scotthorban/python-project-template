# Change Log

All changes to this project will be documented in this file.

This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [semantic versioning](https://semver.org/).

## 2.4.2

- [#16](https://github.com/scotthorban/python-project-template/issues/16) - Add and apply `.gitattributes`.

## 2.4.1

- [#19](https://github.com/scotthorban/python-project-template/issues/19) - Update ruff, ty and common-py to latest
  versions.

## 2.4.0

- [#13](https://github.com/scotthorban/python-project-template/issues/13) - Adds `common-py` as a dependency.
- [#13](https://github.com/scotthorban/python-project-template/issues/13) - Use `common-py` for project badge
  generation.

## 2.3.0

- [#12](https://github.com/scotthorban/python-project-template/issues/12) - Adds `ty` for type checking purposes.

## 2.2.1

- [#10](https://github.com/scotthorban/python-project-template/issues/10) - Updated `README.md` to add more info about
  project repo contents and to detail the use of `uv`.

## 2.2.0

- [#8](https://github.com/scotthorban/python-project-template/issues/8) - Enables all ruff rulesets (including
  pydocstyle), disabling specific rules only.

## 2.1.0

- [#3](https://github.com/scotthorban/python-project-template/issues/3) - Adds a GitHub actions job to create a git tag
  and a GitHub Release when merging to `main`.
- [#3](https://github.com/scotthorban/python-project-template/issues/3) - Removes redundant "Setup python version" step
  from test GitHub actions job

## 2.0.0

- [#1](https://github.com/scotthorban/python-project-template/issues/1) - Replace poetry with uv and tox with uv
  taskipy.
- [#1](https://github.com/scotthorban/python-project-template/issues/1) - Replace isort and black with ruff + pre-commit
  hooks.
- [#1](https://github.com/scotthorban/python-project-template/issues/1) - Rename `projectname` folder to `src`.
- [#1](https://github.com/scotthorban/python-project-template/issues/1) - Added `CHANGELOG.md`.

## 1.0.0

- Initial release of template repository using poetry and tox for environment management, pylint for code linting, black
  for code formatting.
