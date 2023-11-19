import enum
import uuid
from datetime import datetime

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
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(Enum(GroupStatus), nullable=False)  # type: ignore
