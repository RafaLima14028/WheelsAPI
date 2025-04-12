from fastapi import APIRouter

from app.schemas.generic import Message
from app.schemas.sales import AdCreate, AdResponse, AdUpdate


router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=AdResponse)
def create_ad(ad: AdCreate):
    pass


@router.patch("/{ad_id}/", response_model=Message)
def update_ad(ad_id: int, ad: AdUpdate):
    return Message(message='Ad updated successfully!')


@router.delete("/{ad_id}/", response_model=Message)
def delete_ad(ad_id: int):
    return Message(message='Ad deleted successfully!')
