from fastapi import APIRouter

from app.schemas.generic import Message
from app.models.vehicles import TypesVehicle
from app.schemas.vehicles import VehicleCreateRequest, VehicleResponse, VehicleUpdate


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/", response_model=VehicleResponse)
def create_vehicle(vehicle: VehicleCreateRequest):
    pass


@router.patch("/{user_id}/", response_model=Message)
def update_vehicle(user_id: int):
    Message(message='Vehicle updated successfully!')


@router.delete("/{user_id}/", response_model=VehicleResponse)
def delete_vehicle(user_id: int, vehicle: VehicleUpdate):
    pass


@router.get("/{vehicle_id}/", response_model=VehicleResponse)
def get_vehicle_by_id(vehicle_id: int):
    pass


@router.get("/{user_id}/", response_model=list[VehicleResponse])
def get_vehicle_by_user(user_id: int):
    pass


@router.get("/{type_vehicle}/", response_model=list[VehicleResponse])
def get_vehicle_by_type(type_vehicle: TypesVehicle):
    pass


@router.get("/{year}/", response_model=list[VehicleResponse])
def get_vehicle_by_year(year: int):
    pass
