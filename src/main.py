from __future__ import annotations

import argparse
import json
import logging
import sys

from pydantic import ValidationError

from src.config import load_config
from src.logging_setup import setup_logging
from src.models import Task
from src.planner import build_plan

logger = logging.getLogger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ForgeOps planning CLI")
    subparsers = parser.add_subparsers(dest="command")

    plan_parser = subparsers.add_parser("plan", help="Create a plan for a task")
    plan_parser.add_argument("--task", help="Task as JSON string")
    plan_parser.add_argument("--title", help="Task title")
    plan_parser.add_argument("--description", help="Task description")
    plan_parser.add_argument("--priority", type=int, help="Task priority (1-5)")

    return parser.parse_args(argv)


def _task_from_args(args: argparse.Namespace) -> Task:
    base: dict[str, object] = {}

    if args.task:
        try:
            base = json.loads(args.task)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSON for --task: {exc}") from exc

    for key in ("title", "description", "priority"):
        value = getattr(args, key)
        if value is not None:
            base[key] = value

    if "title" not in base or "description" not in base:
        raise SystemExit("Task input requires title and description via --task JSON or --title/--description flags")

    try:
        return Task.model_validate(base)
    except ValidationError as exc:
        raise SystemExit(f"Invalid task input: {exc}") from exc


def cmd_plan(args: argparse.Namespace) -> int:
    task = _task_from_args(args)
    logger.info("building_plan", extra={"event": "plan.start"})
    plan = build_plan(task)
    print(plan.model_dump_json(indent=2))
    logger.info("plan_created", extra={"event": "plan.complete"})
    return 0


def main(argv: list[str] | None = None) -> int:
    config = load_config()
    setup_logging(level=config.log_level, json_logs=config.json_logs)

    args = parse_args(argv)

    if args.command == "plan":
        return cmd_plan(args)

    print("No command provided. Use 'plan'.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
