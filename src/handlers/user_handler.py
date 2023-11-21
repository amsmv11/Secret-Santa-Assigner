from src.models.user import User
from src.services import user_services
from src.values.group_values import CreateGroupRequest


def create_user(
    create_user_request: CreateGroupRequest,
) -> User:
    return user_services.create_user(create_user_request)
