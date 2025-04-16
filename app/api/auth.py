from fastapi import APIRouter, HTTPException, Depends
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.users import User
from app.schemas.auth import Login, Token
from app.core.security import create_access_token, get_current_user, check_hashed_password
from app.core.errors.auth_errors import (
    UNAUTHORIZED_RESPONSE
)


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/", response_model=Token, responses={
    **UNAUTHORIZED_RESPONSE
})
def create_token(login: Login, session: Session = Depends(get_db)):
    user_db = session.scalar(
        select(User).where(
            User.email == login.email
        )
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Invalid authentication credentials!'
        )

    if user_db:
        if not check_hashed_password(login.password, user_db.password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail='Invalid authentication credentials!'
            )

    token = create_access_token(login.email)

    return Token(access_token=token)


@router.post("/refresh-auth/", response_model=Token)
def refresh_token(user: User = Depends(get_current_user)):
    new_token = create_access_token(user.email)

    return Token(access_token=new_token)
