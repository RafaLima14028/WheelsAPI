from fastapi import HTTPException
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.users import UserCreate, UserResponse, UserUpdate
from app.models.users import User

from app.core.security import hash_password


def create_user_in_db(user: UserCreate, session: Session) -> UserResponse:
    password_hashed = hash_password(user.password)

    user_db = User(
        name=user.name,
        email=user.email,
        password=password_hashed
    )

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db


def update_user_in_db(user_id: int, user: UserUpdate, session: Session) -> UserResponse:
    user_db = session.scalar(
        select(User).where(User.id == user_id)
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This user not exists!'
        )

    update_datas = user.dict(exclude_unset=True)

    if 'password' in update_datas.keys():
        password_hashed = hash_password(user.password)

        user_db.password = password_hashed

        del update_datas['password']

    for key, value in update_datas.items():
        setattr(user_db, key, value)

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db


def delete_user_in_db(user_id: int, session: Session) -> None:
    user_db = session.scalar(
        select(User).where(User.id == user_id)
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This user not exists!'
        )

    session.delete(user_db)
    session.commit()


def get_user_by_id_in_db(user_id: int, session: Session) -> UserResponse:
    user_db = session.scalar(
        select(User).where(User.id == user_id)
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This user not exists!'
        )

    return user_db
