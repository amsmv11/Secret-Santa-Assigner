import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from src.models.base import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    group_id = Column(UUID(as_uuid=True), nullable=True)


class User(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    created_at: datetime
    group_id: uuid.UUID | None

    @staticmethod
    def from_model(user_model: UserModel) -> "User":
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            created_at=user_model.created_at,
            group_id=user_model.group_id,
        )
