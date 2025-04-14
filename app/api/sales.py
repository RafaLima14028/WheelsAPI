from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.generic import Message
from app.schemas.sales import AdCreate, AdResponse, AdUpdate
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


router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=AdResponse, responses={
    **NOT_FOUND_VEHICLE_ID_RESPONSE
})
def create_ad(ad: AdCreate, session: Session = Depends(get_db)):
    ad_db = create_ad_in_db(ad, session)

    return ad_db


@router.patch("/{ad_id}/", response_model=AdResponse, responses={
    **NOT_FOUND_RESPONSE
})
def update_ad(ad_id: int, ad: AdUpdate, session: Session = Depends(get_db)):
    ad_db = update_ad_in_db(ad_id, ad, session)

    return ad_db


@router.delete("/{ad_id}/", response_model=Message, responses={
    **NOT_FOUND_RESPONSE
})
def delete_ad(ad_id: int, session: Session = Depends(get_db)):
    delete_ad_in_db(ad_id, session)

    return Message(message='Ad deleted successfully!')


@router.get("/{ad_id}/", response_model=AdResponse, responses={
    **NOT_FOUND_RESPONSE
})
def get_ad_by_id(ad_id: int, session: Session = Depends(get_db)):
    ad_db = get_ad_by_id_in_db(ad_id, session)

    return ad_db
