import logging
from uuid import UUID  # ignore C0114

from fastapi import APIRouter

from src.handlers import group_handler
from src.models.group import Group
from src.values.group_values import CreateGroupRequest

logger = logging.getLogger()

router = APIRouter()


@router.post("", description="Creates a group.")
async def create_group(
    owner_username: str,
    create_group_request: CreateGroupRequest,
) -> Group | None:
    """Endpoint for creating a group."""
    logger.info(f"{create_group_request=}")

    return group_handler.create_group(owner_username, create_group_request)


@router.post("/{group_id}:add_user/{username}", description="Creates a group.")
async def add_user_to_group(
    owner_username: str,
    group_id: UUID,
    username: str,
) -> None:
    """Endpoint for adding an user to a group."""
    logger.info("owner %s, group_id %s, username %s", owner_username, group_id, username)

    group_handler.add_user_to_group(owner_username, group_id, username)


@router.get("", description="Gets all groups for one user.")
async def list_groups(
    owner_username: str,
) -> list[Group] | None:
    """Endpoint for getting all groups for a user."""
    logger.info("owner username %s", owner_username)

    return group_handler.list_groups_by_username(
        owner_username,
    )


@router.post("/{group_id}:assign_secret_santa", description="Assigns secret santas to all users in a group.")
async def assign_secret_santa(
    owner_username: str,
    group_id: UUID,
) -> None:
    """Endpoint for assigning secret santas to all users in a group."""
    logger.info("owner %s, group_id %s", owner_username, group_id)

    group_handler.assign_secret_santa(owner_username, group_id)
