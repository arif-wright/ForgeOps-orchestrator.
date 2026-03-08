"""Planning logic for ForgeOps."""

from src.models import Task


class Planner:
    """Minimal planner stub for initial orchestration flow."""

    def create_plan(self, task: Task) -> dict[str, object]:
        return {
            "task_id": str(task.id),
            "summary": f"Placeholder plan for task: {task.title}",
            "steps": [
                "Validate task input",
                "Select execution agent",
                "Run Codex workflow",
            ],
        }
