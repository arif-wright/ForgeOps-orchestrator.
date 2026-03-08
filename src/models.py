"""Core orchestration models."""

from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Status(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"


class Agent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    model: str
    version: str | None = None
    status: Status = Status.PENDING
    created_at: datetime = Field(default_factory=_utc_now)


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    status: Status = Status.PENDING
    priority: int = 0
    created_at: datetime = Field(default_factory=_utc_now)


class ToolCall(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    arguments: dict[str, object] = Field(default_factory=dict)
    status: Status = Status.PENDING
    started_at: datetime | None = None
    completed_at: datetime | None = None


class Artifact(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    kind: str
    uri: str
    created_at: datetime = Field(default_factory=_utc_now)


class Run(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    agent_id: UUID | None = None
    status: Status = Status.PENDING
    tool_calls: list[ToolCall] = Field(default_factory=list)
    artifacts: list[Artifact] = Field(default_factory=list)
    started_at: datetime | None = None
    completed_at: datetime | None = None
