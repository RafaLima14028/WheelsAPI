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
    id_img: Optional[list[int]]


class VehicleImgCreate(BaseModel):
    img_base64: str


class VehicleCreateRequest(BaseModel):
    vehicle: VehicleCreate
    image: list[VehicleImgCreate] = []


class VehicleResponse(BaseModel):
    id: Optional[int]
    brand: Optional[str]
    model: Optional[str]
    mileage: Optional[int]
    color: Optional[str]
    year_manufacture: Optional[int]
    year_model: Optional[int]
    plate: Optional[str]
    type: Optional[TypesVehicle]
    id_user: Optional[int]
    id_img: Optional[list[int]]


class VehicleUpdate(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    mileage: Optional[int]
    color: Optional[str]
    year_manufacture: Optional[int]
    year_model: Optional[int]
    plate: Optional[str]
    type: Optional[TypesVehicle]
    id_user: Optional[int]
    id_img: Optional[list[int]]
