# ForgeOps

ForgeOps includes a planner CLI that builds an ordered execution plan from a validated task model.

## Usage

Run the planner:

```bash
python -m src.main plan --task '{"title":"Refactor logging","description":"Standardize structured logging across services","priority":2}'
```

You can also pass fields directly:

```bash
python -m src.main plan \
  --title "Refactor logging" \
  --description "Standardize structured logging across services" \
  --priority 2
```

The command validates task input using `Task` and prints a structured plan object with ordered steps.
