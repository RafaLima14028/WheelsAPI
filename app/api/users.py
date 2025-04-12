from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

from sqlalchemy.orm import Session

from app.schemas.generic import Message
from app.schemas.users import UserCreate, UserResponse, UserUpdate

from app.db.session import get_db

from app.crud.users import (
    create_user_in_db,
    update_user_in_db,
    delete_user_in_db,
    get_user_by_id_in_db
)


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, session: Session = Depends(get_db)):
    user_db = create_user_in_db(user_data, session)

    return user_db


@router.patch("/{user_id}/", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    session: Session = Depends(get_db)
):
    user_db = update_user_in_db(user_id, user_data, session)

    return user_db


@router.delete("/{user_id}/", response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_db)):
    delete_user_in_db(user_id, session)

    return Message(message='User deleted successfully!')


@router.get("/{user_id}/", response_model=UserResponse, responses={
    404: {
        'description': 'User not exists in database!',
        'content': {
            'application/json': {
                'example': {'detail': 'This user not exists!'}
            }
        }
    }
})
def get_user_by_id(user_id: int, session: Session = Depends(get_db)):
    user_db = get_user_by_id_in_db(user_id, session)

    return user_db
