from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

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
from app.core.errors.vehicles_errors import (
    NOT_FOUND_RESPONSE,
    UNPROCESSABLE_ENTITY_RESPONSE,
    INTERNAL_SERVER_ERROR_RESPONSE
)
from app.core.errors.security_errors import UNAUTHORIZED_ENTITY_RESPONSE
from app.models.users import User
from app.core.security import get_current_user


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/", response_model=VehicleResponse, responses={
    **NOT_FOUND_RESPONSE,
    **UNPROCESSABLE_ENTITY_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def create_vehicle(
    vehicle: VehicleCreateRequest,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    if vehicle.vehicle.id_user != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    vehicle_db = create_vehicle_in_db(
        vehicle.vehicle,
        vehicle.image,
        session
    )

    return vehicle_db


@router.patch("/{vehicle_id}/", response_model=VehicleUpdate, responses={
    **NOT_FOUND_RESPONSE,
    **INTERNAL_SERVER_ERROR_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def update_vehicle(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    if vehicle_id != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    vehicle_db = update_vehicle_in_db(vehicle_id, vehicle, session)

    return vehicle_db


@router.delete("/{vehicle_id}/", response_model=Message, responses={
    **NOT_FOUND_RESPONSE,
    **INTERNAL_SERVER_ERROR_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def delete_vehicle(
    vehicle_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    if vehicle_id != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    delete_vehicle_in_db(vehicle_id, session)

    return Message(message='Vehicle deleted with successfully!')


@router.get("/{vehicle_id}/", response_model=VehicleResponse, responses={
    **NOT_FOUND_RESPONSE
})
def get_vehicle_by_id(vehicle_id: int, session: Session = Depends(get_db)):
    vehicle_db = get_vehicle_by_id_in_db(vehicle_id, session)

    return vehicle_db


@router.get("/get-by-userid/{user_id}/", response_model=list[VehicleResponse], responses={
    **NOT_FOUND_RESPONSE
})
def get_vehicle_by_user(user_id: int, session: Session = Depends(get_db)):
    vehicles_db = get_vehicle_by_user_in_db(user_id, session)

    return vehicles_db


@router.get("/get-by-type/{type_vehicle}/", response_model=list[VehicleResponse], responses={
    **NOT_FOUND_RESPONSE
})
def get_vehicle_by_type(type_vehicle: TypesVehicle, session: Session = Depends(get_db)):
    vehicles_db = get_vehicle_by_type_in_db(type_vehicle, session)

    return vehicles_db


@router.get("/get-by-year/{year}/", response_model=list[VehicleResponse], responses={
    **NOT_FOUND_RESPONSE
})
def get_vehicle_by_year(year: int, session: Session = Depends(get_db)):
    vehicles_db = get_vehicle_by_year_in_db(year, session)

    return vehicles_db
