import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import select, update

from src.models.user import User, UserModel
from src.services.database import session
from src.values.user_values import CreateUserRequest


def create_user(create_user_request: CreateUserRequest) -> User:
    user = UserModel(
        id=uuid.uuid4(),
        name=create_user_request.name,
        email=create_user_request.email,
        created_at=datetime.utcnow(),
        group_id=None,
    )
    session.add(user)
    session.commit()

    return User.from_model(user)


def get_user_by_email(email: str) -> User | None:
    query = select(UserModel).where(UserModel.email == email)
    user = session.execute(query).unique().scalar_one_or_none()
    session.commit()

    return User.from_model(user)


def get_user_by_name(name: str) -> User | None:
    query = select(UserModel).where(UserModel.name == name)
    user = session.execute(query).unique().scalar_one_or_none()
    session.commit()

    return User.from_model(user)


def get_user_by_id(user_id: UUID) -> User | None:
    query = select(UserModel).where(UserModel.id == user_id)
    user = session.execute(query).unique().scalar_one_or_none()
    session.commit()

    return User.from_model(user)


def associate_user_with_group(user_id: UUID, group_id: UUID) -> None:
    query = update(UserModel).where(UserModel.id == user_id).values(group_id=group_id)
    session.execute(query)
    session.commit()


def list_users_by_group_id(group_id: UUID) -> list[User] | None:
    query = select(UserModel).where(UserModel.group_id == group_id)
    users = session.execute(query).all()
    session.commit()
    return [User.from_model(user) for user in users]
