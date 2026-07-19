# Getting started

## Requirements

- Python 3.10 or newer
- Git
- A virtual environment is recommended

## Clone

```bash
git clone https://github.com/wcalmels/phi47.git
cd phi47
git switch scientific-revision-v0.2
```

## Create a virtual environment

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -e ".[dev]"
```

## Run the validation suite

```powershell
py -m pytest -q
```

## Run the example

```powershell
$env:PYTHONPATH = (Get-Location).Path
py .\examples\basic_usage.py
```

## Run the command-line interface

```powershell
$env:PYTHONPATH = (Get-Location).Path
py -m phi47
```

## Development workflow

Create changes in a dedicated branch, run tests locally, and submit a pull request using the repository template.
