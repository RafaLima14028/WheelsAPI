from typing import Optional
from pydantic import BaseModel


class AdCreate(BaseModel):
    id_vehicle: int
    value: float
    value_fipe: float
    difference_between_value_and_fipe: float


class AdUpdate(BaseModel):
    id_vehicle: int
    value: float
    value_fipe: float
    difference_between_value_and_fipe: float


class AdResponse(BaseModel):
    id: Optional[int]
    id_vehicle: Optional[int]
    value: Optional[float]
    value_fipe: Optional[float]
    difference_between_value_and_fipe: Optional[float]
