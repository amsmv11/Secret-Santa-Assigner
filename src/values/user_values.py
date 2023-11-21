from pydantic import BaseModel

from src.models.user import User


class CreateUserRequest(BaseModel):
    """Request model for creating a user."""

    name: str
    email: str


class SecretSantaUser(BaseModel):
    """Model used to link users in a group for secret santa."""

    santa: User
    surprisee: User = None
