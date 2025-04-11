from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from ..db.session import Base


@Base.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
