from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=2000)
    priority: int = Field(default=3, ge=1, le=5)


class PlanStep(BaseModel):
    id: int = Field(..., ge=1)
    summary: str = Field(..., min_length=1, max_length=300)
    status: Literal["pending", "in_progress", "completed"] = "pending"


class Plan(BaseModel):
    task: Task
    steps: list[PlanStep] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
