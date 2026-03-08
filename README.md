# ForgeOps

ForgeOps is a cloud-hosted AI orchestration system that runs coding tasks through Codex on a self-hosted GitHub runner.

## Scope (Initial Skeleton)

This repository currently contains a minimal Python project foundation:

- Environment-driven configuration loading
- Structured logging setup
- First-pass domain models for orchestration entities
- A minimal planner stub
- A CLI entrypoint for startup wiring

## Project Structure

```text
.
├── .env.example
├── requirements.txt
├── README.md
└── src
    ├── __init__.py
    ├── config.py
    ├── logging_setup.py
    ├── main.py
    ├── models.py
    └── planner.py
```

## Quick Start

1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Copy `.env.example` to `.env` and update values.
4. Run the CLI:

```bash
python -m src.main
```
