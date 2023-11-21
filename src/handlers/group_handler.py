import random
from uuid import UUID

from fastapi import HTTPException

from src.models.group import Group
from src.services import group_services, user_services
from src.values.group_values import CreateGroupRequest
from src.values.user_values import SecretSantaUser


def create_group(
    owner_username: str,
    create_group_request: CreateGroupRequest,
) -> Group:
    return group_services.create_group(owner_username, create_group_request)


def add_user_to_group(
    owner_username: str,
    group_id: UUID,
    username: str,
) -> Group:
    owner_user = user_services.get_user_by_name(owner_username)
    user = user_services.get_user_by_name(username)
    group = group_services.get_group_by_id(group_id)
    if user is None or group is None:
        raise HTTPException(
            status_code=404,
            detail="User or Group not found",
        )
    if group.owner_id != owner_user.id:
        raise HTTPException(
            status_code=403,
            detail="User is not the owner of the group",
        )

    return user_services.associate_user_with_group(user.id, group_id)


def list_groups_by_username(
    owner_username: str,
) -> list[Group] | None:
    owner_user = user_services.get_user_by_name(owner_username)
    if owner_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    return group_services.list_groups_by_username(owner_user.id)


def assign_secret_santa(
    owner_username: str,
    group_id: UUID,
) -> None:
    owner_user = user_services.get_user_by_name(owner_username)
    group = group_services.get_group_by_id(group_id)
    if group is None:
        raise HTTPException(
            status_code=404,
            detail="Group not found",
        )
    if group.owner_id != owner_user.id:
        raise HTTPException(
            status_code=403,
            detail="User is not the owner of the group",
        )

    all_users = user_services.list_users_by_group_id(group_id)
    if len(all_users) < 3 or not all_users:
        raise HTTPException(
            status_code=403,
            detail="Not enough users in the group",
        )

    first_user = random.choice(all_users)
    all_users.remove(first_user)

    assigned_users = []

    user = SecretSantaUser(santa=first_user)

    while len(all_users) > 0:
        user.surprisee = random.choice(all_users)
        all_users.remove(user.surprisee)
        assigned_users.append(user)

        user = SecretSantaUser(santa=user.surprisee)

    user.surprisee = first_user
    assigned_users.append(user)

    # TODO take the assigned users and send emails to them
