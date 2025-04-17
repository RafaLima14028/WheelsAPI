from typing import Optional
from pydantic import BaseModel


class AdCreate(BaseModel):
    id_vehicle: int
    value: float


class AdUpdate(BaseModel):
    value: float


class AdResponse(BaseModel):
    id: Optional[int] = None
    id_vehicle: Optional[int] = None
    value: Optional[float] = None
    value_fipe: Optional[float] = None
    difference_between_value_and_fipe: Optional[float] = None


class VehicleSaleResponse(BaseModel):
    id_vehicle: Optional[int] = None
    id_sale: Optional[int] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    year_model: Optional[int] = None
    plate: Optional[str] = None
    value: Optional[float] = None
    value_fipe: Optional[float] = None
    difference_between_value_and_fipe: Optional[float] = None


class GetSalesVehiclesResponse(BaseModel):
    vehicles: list[VehicleSaleResponse] = []
    nextUrl: Optional[str] = None
    previousUrl: Optional[str] = None
    limit: int
    offset: int
    totalRegistries: int
