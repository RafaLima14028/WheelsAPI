from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

from sqlalchemy.orm import Session

from app.schemas.generic import Message
from app.schemas.users import UserCreate, UserResponse, UserUpdate
from app.models.users import User
from app.db.session import get_db
from app.core.security import get_current_user
from app.crud.users import (
    create_user_in_db,
    update_user_in_db,
    delete_user_in_db,
    get_user_by_id_in_db
)
from app.core.errors.users_errors import NOT_FOUND_RESPONSE
from app.core.errors.security_errors import UNAUTHORIZED_ENTITY_RESPONSE


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, session: Session = Depends(get_db)):
    user_db = create_user_in_db(user_data, session)

    return user_db


@router.patch("/{user_id}/", response_model=UserResponse, responses={
    **NOT_FOUND_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def update_user(
    user_id: int,
    user_data: UserUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    if user_id != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    user_db = update_user_in_db(user_id, user_data, session)

    return user_db


@router.delete("/{user_id}/", response_model=Message, responses={
    **NOT_FOUND_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def delete_user(
    user_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    if user_id != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    delete_user_in_db(user_id, session)

    return Message(message='User deleted successfully!')


@router.get("/{user_id}/", response_model=UserResponse, responses={
    **NOT_FOUND_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def get_user_by_id(
    user_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    if user_id != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    user_db = get_user_by_id_in_db(user_id, session)

    return user_db
