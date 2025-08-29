## Python Project Template

![](docs/img/python.svg)
![](docs/img/unittest.svg)
![](docs/img/coverage.svg)
![](docs/img/ruff.svg)
![](docs/img/release.svg)

### 1. Description
A repository template for python projects.

### 2. Installation

#### 2.1 Pre-Requisites
This project template uses [uv](https://docs.astral.sh/uv/) for package and project management. 

```shell
# Install dependencies using uv
uv sync --all-extras --dev

# Install pre-commit hooks
uv run task install-hooks

# View other uv tasks
uv run task --list
```

### 3. Local Run
```shell
cd projectname
python run_project.py
```
