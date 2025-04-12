from sqlalchemy import create_engine
from sqlalchemy.orm import Session, registry

from app.core.settings import Settings


Base = registry()


def get_db():
    engine = create_engine(Settings().DATABASE_URL)

    with Session(engine) as session:
        yield session
