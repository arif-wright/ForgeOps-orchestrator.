from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict

from .models import Task, TaskValidationError
from .planner import build_plan


def _load_task_from_args(args: argparse.Namespace) -> Task:
    task_payload: Dict[str, Any]

    if args.task:
        try:
            parsed = json.loads(args.task)
        except json.JSONDecodeError as exc:
            raise TaskValidationError(f"Invalid JSON for --task: {exc.msg}") from exc
        if not isinstance(parsed, dict):
            raise TaskValidationError("--task must decode to a JSON object")
        task_payload = parsed
    else:
        task_payload = {
            "title": args.title,
            "description": args.description,
            "priority": args.priority,
        }

    return Task.from_dict(task_payload)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ForgeOps planner CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan", help="Create an ordered plan for a task")
    plan_parser.add_argument(
        "--task",
        type=str,
        help="Task as a JSON object, e.g. '{\"title\":\"X\",\"description\":\"Y\",\"priority\":2}'",
    )
    plan_parser.add_argument("--title", type=str, help="Task title")
    plan_parser.add_argument("--description", type=str, help="Task description")
    plan_parser.add_argument("--priority", type=int, help="Task priority (1-5)")

    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "plan":
        try:
            task = _load_task_from_args(args)
            plan = build_plan(task)
        except TaskValidationError as exc:
            print(f"Task validation failed: {exc}", file=sys.stderr)
            return 2

        print(json.dumps(plan.to_dict(), indent=2))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
