from fastapi import HTTPException
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.vehicles import Vehicle, VehicleImg, TypesVehicle
from app.models.users import User
from app.schemas.vehicles import (
    VehicleCreate,
    VehicleImgCreate,
    VehicleResponse,
    VehicleUpdate
)


def create_vehicle_in_db(
    vehicle: VehicleCreate,
    vehicle_img: VehicleImgCreate,
    session: Session
) -> VehicleResponse:
    try:
        user_db = session.scalar(
            select(User).where(User.id == vehicle.id_user)
        )

        if not user_db:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="The user ID does not exist!"
            )

        vehicle_db = Vehicle(
            brand=vehicle.brand,
            model=vehicle.model,
            mileage=vehicle.mileage,
            color=vehicle.color,
            year_manufacture=vehicle.year_manufacture,
            year_model=vehicle.year_model,
            plate=vehicle.plate,
            type=vehicle.type,
            id_user=vehicle.id_user
        )

        session.add(vehicle_db)
        session.flush()

        id_vehicle = vehicle_db.id

        list_imgs = vehicle_img.dict().get("list_imgs", [])

        for img in list_imgs:
            img_db = VehicleImg(
                img_base64=img,
                id_vehicle=id_vehicle
            )

            session.add(img_db)

        session.commit()
        session.refresh(vehicle_db)

        return vehicle_db
    except Exception as e:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Unable to process the provided data!"
        )


def update_vehicle_in_db(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    session: Session
) -> VehicleResponse:
    vehicle_db = session.scalar(
        select(Vehicle).where(Vehicle.id == vehicle_id)
    )

    if not vehicle_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This vehicle does not exist!'
        )

    try:
        vehicle_data_update = vehicle.dict(exclude_unset=True)

        for key, value in vehicle_data_update.items():
            setattr(vehicle_db, key, value)

        session.add(vehicle_db)
        session.commit()
        session.refresh(vehicle_db)

        return vehicle_db
    except Exception:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='An error has occurred!'
        )


def delete_vehicle_in_db(vehicle_id: int, session: Session) -> bool:
    vehicle_db = session.scalar(
        select(Vehicle).where(Vehicle.id == vehicle_id)
    )

    if not vehicle_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This vehicle does not exist!'
        )

    vehicle_imgs_db = session.scalars(
        select(VehicleImg).where(VehicleImg.id_vehicle == vehicle_id)
    )

    try:
        if vehicle_imgs_db:
            for obj_vehicle_imgs in vehicle_imgs_db:
                session.delete(obj_vehicle_imgs)

            session.flush()

        session.delete(vehicle_db)
        session.commit()

        return True
    except Exception:
        session.rollback()

        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='An error has occurred!'
        )


def get_vehicle_by_id_in_db(vehicle_id: int, session: Session) -> VehicleResponse:
    vehicle_db = session.scalar(
        select(Vehicle).where(Vehicle.id == vehicle_id)
    )

    if not vehicle_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This vehicle does not exist!'
        )

    return vehicle_db


def get_vehicle_by_user_in_db(user_id: int, session: Session) -> list[VehicleResponse]:
    vehicles_db = session.scalars(
        select(Vehicle).where(Vehicle.id_user == user_id)
    )

    if not vehicles_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This user id does not has vehicles!'
        )

    return vehicles_db


def get_vehicle_by_type_in_db(type_vehicle: TypesVehicle, session: Session) -> list[VehicleResponse]:
    vehicles_db = session.scalars(
        select(Vehicle).where(Vehicle.type == type_vehicle)
    )

    if not vehicles_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This type of vehicle does not exist!'
        )

    return vehicles_db


def get_vehicle_by_year_in_db(year: int, session: Session) -> list[VehicleResponse]:
    vehicles_db = session.scalars(
        select(Vehicle).where(Vehicle.year_model == year)
    )

    if not vehicles_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='This year of vehicle does not exist!'
        )

    return vehicles_db
