from fastapi import APIRouter, HTTPException, Depends
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.users import User
from app.models.auth import Login, Token
from app.core.security import create_access_token, get_current_user


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/", response_model=Token)
def create_token(login: Login, session: Session = Depends(get_db)):
    user_db = session.scalar(
        select(User).where(
            User.email == login.email,
            User.password == login.password
        )
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Invalid authentication credentials!'
        )

    token = create_access_token(login.email)

    return Token(access_token=token)
