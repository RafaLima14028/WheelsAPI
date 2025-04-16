from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.generic import Message
from app.schemas.sales import AdCreate, AdResponse, AdUpdate, VehicleSaleResponse
from app.db.session import get_db
from app.crud.sales import (
    create_ad_in_db,
    update_ad_in_db,
    delete_ad_in_db,
    get_ad_by_id_in_db
)
from app.core.errors.sales_errors import (
    NOT_FOUND_RESPONSE,
    NOT_FOUND_VEHICLE_ID_RESPONSE
)
from app.core.errors.security_errors import UNAUTHORIZED_ENTITY_RESPONSE
from app.models.users import User
from app.models.vehicles import TypesVehicle, Vehicle
from app.models.sales import Sale
from app.core.security import get_current_user


router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=AdResponse, responses={
    **NOT_FOUND_VEHICLE_ID_RESPONSE
})
def create_ad(
    ad: AdCreate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    vehicle_db = session.scalar(
        select(Vehicle).where(Vehicle.id == ad.id_vehicle)
    )

    if vehicle_db.id_user != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    ad_db = create_ad_in_db(ad, session)

    return ad_db


@router.patch("/{ad_id}/", response_model=AdResponse, responses={
    **NOT_FOUND_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def update_ad(
    ad_id: int,
    ad: AdUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    vehicle_db = session.execute(
        select(Vehicle)
        .join(Vehicle, Sale.id_vehicle == Vehicle.id)
        .where(Sale.id == ad_id)
    )

    if vehicle_db.id_user != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    ad_db = update_ad_in_db(ad_id, ad, session)

    return ad_db


@router.delete("/{ad_id}/", response_model=Message, responses={
    **NOT_FOUND_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def delete_ad(
    ad_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    vehicle_db = session.execute(
        select(Vehicle)
        .join(Vehicle, Sale.id_vehicle == Vehicle.id)
        .where(Sale.id == ad_id)
    )

    if vehicle_db.id_user != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    delete_ad_in_db(ad_id, session)

    return Message(message='Ad deleted successfully!')


@router.get("ad/{ad_id}/", response_model=AdResponse, responses={
    **NOT_FOUND_RESPONSE,
    **UNAUTHORIZED_ENTITY_RESPONSE
})
def get_ad_by_id(
    ad_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    vehicle_db = session.execute(
        select(Vehicle)
        .join(Vehicle, Sale.id_vehicle == Vehicle.id)
        .where(Sale.id == ad_id)
    )

    if vehicle_db.id_user != user.id:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Divergent data!'
        )

    ad_db = get_ad_by_id_in_db(ad_id, session)

    return ad_db


@router.get("/sales-vehicles/", response_model=list[VehicleSaleResponse])
def get_sales_vehicles(
    limit: int = 10,
    offset: int = 0,
    type: Optional[TypesVehicle] = None,
    min_year: Optional[int] = None,
    max_year: Optional[int] = None,
    max_mileage: Optional[int] = None,
    color: Optional[str] = None,
    session: Session = Depends(get_db)
):
    query = select(Vehicle, Sale).join(Sale, Vehicle.id == Sale.id_vehicle)

    if type:
        query = query.where(Vehicle.type == type)
    if min_year:
        query = query.where(Vehicle.model >= min_year)
    if max_year:
        query = query.where(Vehicle.model <= max_year)
    if max_mileage:
        query = query.where(Vehicle.mileage <= max_mileage)
    if color:
        query = query.where(Vehicle.color == color)

    query = query.limit(limit).offset(offset)

    results = session.execute(query).all()

    response = []

    for vehicle, sale in results:
        response.append(
            VehicleSaleResponse(
                id_vehicle=vehicle.id,
                id_sale=sale.id,
                brand=vehicle.brand,
                model=vehicle.model,
                color=vehicle.color,
                year_model=vehicle.year_model,
                plate=vehicle.plate,
                value=sale.value,
                value_fipe=sale.value_fipe,
                difference_between_value_and_fipe=sale.difference_between_value_and_fipe
            )
        )

    return response
