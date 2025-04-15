from fastapi import HTTPException, Depends
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

import bcrypt
import jwt
from jwt.exceptions import ExpiredSignatureError, DecodeError, PyJWTError
from cryptography.hazmat.primitives import serialization

from datetime import datetime, timedelta

from app.core.settings import Settings
from app.db.session import get_db
from app.models.users import User


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()

    password_hashed = bcrypt.hashpw(
        password.encode('utf-8'),
        salt
    )\
        .decode('utf-8')

    return password_hashed


def check_hashed_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )


def create_access_token(email: str) -> str:
    exp = datetime.now() + timedelta(
        minutes=Settings().EXPIRE_TIME_JWT
    )

    payload = {
        'exp': exp,
        'sub': email
    }

    token = jwt.encode(
        payload=payload,
        key=Settings().PRIVATE_KEY,
        algorithm='HS256'
    )

    return token


def get_current_user(token: str, session: Session = Depends(get_db)) -> str:
    header_data = jwt.get_unverified_header(token)

    try:
        payload: dict = jwt.decode(
            token,
            key=Settings().PRIVATE_KEY,
            algorithms=[header_data['alg'], ]
        )

        email = payload.get('sub', None)
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Your credentials have expired!'
        )
    except DecodeError:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='An error occurred in the decoding!'
        )
    except PyJWTError:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='An error occurred!'
        )

    user_db = session.scalar(
        select(User).where(User.email == email)
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Invalid authentication credentials!'
        )

    return email
