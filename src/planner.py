from __future__ import annotations

from src.models import Plan, PlanStep, Task


PRIORITY_LABELS = {
    1: "critical",
    2: "high",
    3: "normal",
    4: "low",
    5: "backlog",
}


def build_plan(task: Task) -> Plan:
    """Create a deterministic, implementation-oriented plan for a task."""
    priority_label = PRIORITY_LABELS.get(task.priority, "normal")

    steps = [
        PlanStep(id=1, summary=f"Clarify scope and acceptance criteria for '{task.title}'."),
        PlanStep(
            id=2,
            summary=f"Implement changes for priority {task.priority} ({priority_label}) task requirements.",
        ),
        PlanStep(id=3, summary="Validate behavior with compile/runtime smoke checks."),
    ]

    if task.priority <= 2:
        steps.insert(
            3,
            PlanStep(
                id=4,
                summary="Add hardening checks for edge cases before merge.",
            ),
        )
        for idx, step in enumerate(steps, start=1):
            step.id = idx

    return Plan(task=task, steps=steps)
