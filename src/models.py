from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


class TaskValidationError(ValueError):
    """Raised when task input fails validation."""


@dataclass(frozen=True)
class Task:
    title: str
    description: str
    priority: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        title = data.get("title")
        description = data.get("description")
        priority = data.get("priority")

        if not isinstance(title, str) or not title.strip():
            raise TaskValidationError("'title' must be a non-empty string")
        if not isinstance(description, str) or not description.strip():
            raise TaskValidationError("'description' must be a non-empty string")

        if isinstance(priority, bool) or not isinstance(priority, int):
            raise TaskValidationError("'priority' must be an integer between 1 and 5")
        if priority < 1 or priority > 5:
            raise TaskValidationError("'priority' must be between 1 and 5")

        return cls(title=title.strip(), description=description.strip(), priority=priority)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
        }


@dataclass(frozen=True)
class PlanStep:
    order: int
    action: str

    def to_dict(self) -> Dict[str, Any]:
        return {"order": self.order, "action": self.action}


@dataclass(frozen=True)
class Plan:
    task: Task
    steps: List[PlanStep]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task": self.task.to_dict(),
            "steps": [step.to_dict() for step in self.steps],
        }
