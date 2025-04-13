from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.generic import Message
from app.models.vehicles import TypesVehicle
from app.schemas.vehicles import (
    VehicleCreateRequest,
    VehicleResponse,
    VehicleUpdate
)
from app.crud.vehicles import (
    create_vehicle_in_db,
    update_vehicle_in_db,
    delete_vehicle_in_db,
    get_vehicle_by_id_in_db,
    get_vehicle_by_user_in_db,
    get_vehicle_by_type_in_db,
    get_vehicle_by_year_in_db
)


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreateRequest,
    session: Session = Depends(get_db)
):
    vehicle_db = create_vehicle_in_db(
        vehicle.vehicle,
        vehicle.image,
        session
    )

    return vehicle_db


@router.patch("/{vehicle_id}/", response_model=VehicleUpdate)
def update_vehicle(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    session: Session = Depends(get_db)
):
    vehicle_db = update_vehicle_in_db(vehicle_id, vehicle, session)

    return vehicle_db


@router.delete("/{vehicle_id}/", response_model=Message)
def delete_vehicle(vehicle_id: int, session: Session = Depends(get_db)):
    delete_vehicle_in_db(vehicle_id, session)

    return Message(message='Vehicle deleted with successfully!')


@router.get("/{vehicle_id}/", response_model=VehicleResponse)
def get_vehicle_by_id(vehicle_id: int, session: Session = Depends(get_db)):
    vehicle_db = get_vehicle_by_id_in_db(vehicle_id, session)

    return vehicle_db


@router.get("/get-by-userid/{user_id}/", response_model=list[VehicleResponse])
def get_vehicle_by_user(user_id: int, session: Session = Depends(get_db)):
    vehicles_db = get_vehicle_by_user_in_db(user_id, session)

    return vehicles_db


@router.get("/get-by-type/{type_vehicle}/", response_model=list[VehicleResponse])
def get_vehicle_by_type(type_vehicle: TypesVehicle, session: Session = Depends(get_db)):
    vehicles_db = get_vehicle_by_type_in_db(type_vehicle, session)

    return vehicles_db


@router.get("/get-by-year/{year}/", response_model=list[VehicleResponse])
def get_vehicle_by_year(year: int, session: Session = Depends(get_db)):
    vehicles_db = get_vehicle_by_year_in_db(year, session)

    return vehicles_db
