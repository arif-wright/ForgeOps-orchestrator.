# ForgeOps Orchestrator

ForgeOps is a CLI-first Python planning service that builds execution plans from task input.

## Features

- CLI planning flow via `python -m src.main plan`
- Pydantic models for validated task and plan data
- Config module for environment-driven settings
- Structured logging setup for production-oriented logging output
- Local file-based `RunRepository` for persisting run metadata in `runs/*.json`

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

Use the local run repository (programmatic usage):

```python
from src.repository import RunRepository

repo = RunRepository("runs")
repo.save_run("run_001", {"status": "completed", "task": "Refactor logging"})
run_data = repo.load_run("run_001")
run_ids = repo.list_runs()
```

Notes:

- Run metadata is stored as JSON files under `runs/`.
- `save_run(run_id, data)` writes atomically to reduce partial-write risk.
- `load_run(run_id)` returns `None` when a run does not exist.
- `list_runs()` returns known run IDs (filename stems).

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
