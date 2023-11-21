import enum
import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Enum, String
from sqlalchemy.dialects.postgresql import UUID

from src.models.base import Base


class GroupStatus(enum.Enum):
    created = "created"
    in_progress = "in_progress"
    done = "done"
    failed = "failed"


class GroupModel(Base):
    __tablename__ = "group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, index=True)
    owner_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(Enum(GroupStatus), nullable=False)  # type: ignore
    description = Column(String, nullable=False, index=True)


class Group(BaseModel):
    id: uuid.UUID
    name: str
    owner_id: uuid.UUID
    created_at: datetime
    status: GroupStatus
    description: str

    @staticmethod
    def from_model(group_model: GroupModel) -> "Group":
        return Group(
            id=group_model.id,
            name=group_model.name,
            owner_id=group_model.owner_id,
            created_at=group_model.created_at,
            status=group_model.status,
            description=group_model.description,
        )
