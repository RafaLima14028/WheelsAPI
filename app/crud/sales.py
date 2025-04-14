from fastapi import HTTPException
from http import HTTPStatus
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.schemas.sales import AdCreate, AdUpdate, AdResponse
from app.models.sales import Sale
from app.models.vehicles import Vehicle


def create_ad_in_db(ad: AdCreate, session: Session) -> AdResponse:
    vehicle_db = session.scalar(
        select(Vehicle).where(Vehicle.id == ad.id_vehicle)
    )

    if not vehicle_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Not found the vehicle ID!'
        )

    sale_db = Sale(
        id_vehicle=ad.id_vehicle,
        value=ad.value,
        value_fipe=10000,
        difference_between_value_and_fipe=2000
    )

    session.add(sale_db)
    session.commit()
    session.refresh(sale_db)

    return sale_db


def update_ad_in_db(ad_id: int, ad: AdUpdate, session: Session) -> AdResponse:
    ad_db = session.scalar(
        select(Sale).where(Sale.id == ad_id)
    )

    if not ad_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Not found the ad ID!'
        )

    ad_update_data = ad.dict(exclude_unset=True)

    for key, value in ad_update_data.items():
        setattr(ad_db, key, value)

    session.add(ad_db)
    session.commit()
    session.refresh(ad_db)

    return ad_db


def delete_ad_in_db(ad_id: int, session: Session) -> bool:
    ad_db = session.scalar(
        select(Sale).where(Sale.id == ad_id)
    )

    if not ad_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Not found the ad ID!'
        )

    session.delete(ad_db)
    session.commit()

    return True


def get_ad_by_id_in_db(ad_id: int, session: Session) -> AdResponse:
    ad_db = session.scalar(
        select(Sale).where(Sale.id == ad_id)
    )

    if not ad_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Not found the ad ID!'
        )

    return ad_db
