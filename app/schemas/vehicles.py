from typing import Optional
from pydantic import BaseModel

from app.models.vehicles import TypesVehicle


class VehicleCreate(BaseModel):
    brand: str
    model: str
    mileage: int
    color: str
    year_manufacture: int
    year_model: int
    plate: str
    type: TypesVehicle
    id_user: int


class VehicleImgCreate(BaseModel):
    list_imgs: list[str]


class VehicleCreateRequest(BaseModel):
    vehicle: VehicleCreate
    image: Optional[VehicleImgCreate]


class VehicleResponse(BaseModel):
    id: Optional[int] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    year_model: Optional[int] = None
    plate: Optional[str] = None


class VehicleUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    mileage: Optional[int] = None
    color: Optional[str] = None
    year_manufacture: Optional[int] = None
    year_model: Optional[int] = None
    plate: Optional[str] = None
    type: Optional[TypesVehicle] = None
