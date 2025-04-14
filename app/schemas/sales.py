from typing import Optional
from pydantic import BaseModel


class AdCreate(BaseModel):
    id_vehicle: int
    value: float


class AdUpdate(BaseModel):
    value: float


class AdResponse(BaseModel):
    id: Optional[int]
    id_vehicle: Optional[int]
    value: Optional[float]
    value_fipe: Optional[float]
    difference_between_value_and_fipe: Optional[float]
