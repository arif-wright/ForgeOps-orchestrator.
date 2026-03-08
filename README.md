# ForgeOps Orchestrator

ForgeOps is a CLI-first Python planning service that builds execution plans from task input.

## Features

- CLI planning flow via `python -m src.main plan`
- Pydantic models for validated task and plan data
- Config module for environment-driven settings
- Structured logging setup for production-oriented logging output

## Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

Create a plan from JSON task input:

```bash
python -m src.main plan --task '{"title":"Refactor logging","description":"Standardize structured logging across services","priority":2}'
```

Create a plan from flags:

```bash
python -m src.main plan \
  --title "Refactor logging" \
  --description "Standardize structured logging across services" \
  --priority 2
```

## Configuration

Environment variables:

- `FORGEOPS_APP_NAME` (default: `forgeops`)
- `FORGEOPS_ENV` (default: `dev`)
- `FORGEOPS_LOG_LEVEL` (default: `INFO`)
- `FORGEOPS_JSON_LOGS` (default: `true`)

## Validation and smoke test compatibility

The current workflow remains compatible with:

```bash
python -m py_compile src/main.py src/models.py src/planner.py
python -m src.main plan --title "Refactor logging" --description "Standardize structured logging across services" --priority 2
```

## Scope

This iteration intentionally remains CLI-only and does not add Docker, databases, queues, or web APIs.
