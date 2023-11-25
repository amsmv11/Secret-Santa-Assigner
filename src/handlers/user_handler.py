import uuid
from datetime import datetime
from logging import Logger

from fastapi import HTTPException

from src.models.user import User, UserModel
from src.services import user_services
from src.values.user_values import CreateUserRequest

logger = Logger("user_handler")


def create_user(
    create_user_request: CreateUserRequest,
) -> User | None:
    try:
        user = UserModel(
            id=uuid.uuid4(),
            name=create_user_request.name,
            email=create_user_request.email,
            created_at=datetime.utcnow(),
            group_id=None,
        )
        user_created = user_services.create_user(user)
        return user_created
    except BaseException as e:
        logger.error(e)
        raise HTTPException(
            status_code=400,
            detail=f"Failed to create user {e}",
        )
