from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from enum import Enum

from ..db.session import Base


class TypesVehicle(str, Enum):
    car = "car"
    truck = "truck"
    bus = "bus"
    bike = "bike"
    jet_ski = "jet ski"


@Base.mapped_as_dataclass
class Vehicle:
    __tablename__ = 'vehicles'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
        init=False
    )
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    mileage: Mapped[int] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    year_manufacture: Mapped[int] = mapped_column(nullable=False)
    year_model: Mapped[int] = mapped_column(nullable=False)
    plate: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[TypesVehicle] = mapped_column(
        ENUM(TypesVehicle, create_type=True, name="types_vehicle"),
        nullable=False
    )
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))


@Base.mapped_as_dataclass
class VehicleImg:
    __tablename__ = 'vehicles_img'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        autoincrement=True,
        init=False
    )
    img_base64: Mapped[str] = mapped_column()
    id_vehicle: Mapped[int] = mapped_column(
        ForeignKey('vehicles.id'),
        nullable=False
    )
