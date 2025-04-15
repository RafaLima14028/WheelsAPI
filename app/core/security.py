from fastapi import HTTPException
from http import HTTPStatus

import bcrypt
import jwt
from jwt.exceptions import ExpiredSignatureError, DecodeError, PyJWTError
from cryptography.hazmat.primitives import serialization

from datetime import datetime, timedelta

from app.core.settings import Settings


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
    password = Settings().PRIVATE_KEY_PASSWORD.encode()

    private_key = open(".ssh/id_rsa", 'r').read()
    key = serialization.load_ssh_private_key(
        private_key.encode(),
        password=password
    )

    exp = datetime.now() + timedelta(
        minutes=Settings().EXPIRE_TIME_JWT
    )

    payload = {
        'exp': exp,
        'sub': email
    }

    token = jwt.encode(
        payload=payload,
        key=key,
        algorithm='RS256'
    )

    return token


def get_current_user(token: str) -> str:
    header_data = jwt.get_unverified_header(token)

    public_key = open(".ssh/id_rsa.pub", 'r').read()
    key = serialization.load_ssh_public_key(
        public_key.encode()
    )

    try:
        payload: dict = jwt.decode(
            token,
            key=key,
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

    return email
