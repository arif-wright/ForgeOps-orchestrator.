from __future__ import annotations

from typing import List

from .models import Plan, PlanStep, Task


def build_plan(task: Task) -> Plan:
    """Create an ordered execution plan for a validated task."""
    steps: List[str] = [
        f"Clarify acceptance criteria for '{task.title}'.",
        "Break implementation into small, testable changes.",
        "Implement changes and add or update tests.",
        "Run validation checks and document rollout notes.",
    ]

    if task.priority <= 2:
        steps.insert(1, "Assess delivery risk and define a rollback strategy.")

    ordered_steps = [PlanStep(order=index, action=action) for index, action in enumerate(steps, start=1)]
    return Plan(task=task, steps=ordered_steps)
