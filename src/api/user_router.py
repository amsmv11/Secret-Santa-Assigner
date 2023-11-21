import logging  # ignore C0114

from fastapi import APIRouter

from src.handlers import user_handler
from src.models.user import User
from src.values.user_values import CreateUserRequest

logger = logging.getLogger()

router = APIRouter()


@router.post("", description="Creates a user.")
async def create_user(
    create_user_request: CreateUserRequest,
) -> User:
    """Endpoint for creating a user."""
    logger.info(f"{create_user_request=}")

    return user_handler.create_user(create_user_request)
