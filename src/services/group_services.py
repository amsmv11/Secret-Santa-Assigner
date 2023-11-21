import logging
import uuid
from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select

from src.models.group import Group, GroupModel, GroupStatus
from src.services.database import session
from src.services.user_services import associate_user_with_group, get_user_by_name
from src.values.group_values import CreateGroupRequest

logger = logging.getLogger()


def create_group(
    owner_username: str,
    create_group_request: CreateGroupRequest,
) -> Group | None:
    try:
        user = get_user_by_name(owner_username)
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        group = GroupModel(
            id=uuid.uuid4(),
            name=create_group_request.name,
            created_at=datetime.utcnow(),
            status=GroupStatus.created.name,
            description=create_group_request.description,
            owner_id=user.id,
        )
        session.add(group)
        session.commit()

        associate_user_with_group(user.id, group.id)

        return Group.from_model(group)
    except BaseException as e:
        logger.error(e)
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error: failed to create group",
        )


def get_group_by_id(group_id: uuid.UUID) -> Group | None:
    query = select(GroupModel).filter(GroupModel.id == group_id)
    group = session.execute(query).unique().scalar_one_or_none()
    session.commit()
    return Group.from_model(group)


def list_groups_by_username(owner_id: uuid.UUID) -> list[Group] | None:
    query = select(GroupModel).filter(GroupModel.owner_id == owner_id)
    groups = session.execute(query).all()
    session.commit()
    return [Group.from_model(group) for group in groups]
