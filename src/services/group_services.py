import logging
import uuid

from fastapi import HTTPException
from sqlalchemy import select

from src.models.group import Group, GroupModel
from src.models.user import User
from src.services.database import session
from src.services.user_services import associate_user_with_group

logger = logging.getLogger()


def create_group(
    user: User,
    group: GroupModel,
) -> Group | None:
    try:
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

    if not groups:
        return None

    return [Group.from_model(group[0]) for group in groups]
