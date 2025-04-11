from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..db.session import Base


@Base.mapped_as_dataclass
class VehicleImg:
    __tablename__ = 'vehicles_img'

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True
    )
    img_base64: Mapped[str] = mapped_column()


@Base.mapped_as_dataclass
class Vehicle:
    __tablename__ = 'vehicles'

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True
    )
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    mileage: Mapped[int] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    year_manufacture: Mapped[int] = mapped_column(nullable=False)
    year_model: Mapped[int] = mapped_column(nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    id_img: Mapped[list[int]] = mapped_column(
        ForeignKey('vehicles_img.id'), nullable=True
    )
