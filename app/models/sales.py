from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from ..db.session import Base


@Base.mapped_as_dataclass
class Sale:
    __tablename__ = 'sales'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
        init=False
    )
    id_vehicle: Mapped[int] = mapped_column(
        ForeignKey('vehicles.id'),
        nullable=False
    )
    value: Mapped[float] = mapped_column(nullable=False)
    value_fipe: Mapped[float] = mapped_column(nullable=False)
    difference_between_value_and_fipe: Mapped[float] = mapped_column(
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now(),
        server_onupdate=func.now()
    )
