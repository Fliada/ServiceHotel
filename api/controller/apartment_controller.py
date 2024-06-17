from fastapi import HTTPException, APIRouter

from dao import Reservation
from utils.schemas import *
from config import helper

apartment_routes = APIRouter()


@apartment_routes.post("/available", response_model=list[ApartmentsResponse])
async def get_all_available_apartments(request: AvailableApartmentsRequest):
    try:
        apartments = helper.get_available_apartments(request.start_date, request.end_date, request.city,
                                                     request.capacity, request.hotel_name, request.type_name)

        result_apartments = []
        for ap in apartments:
            apartments_info = {
                "id": ap.id,
                "number": ap.number,
                "hotel_name": ap.hotel.name,
                "hotel_city": ap.hotel.city,
                "cost": ap.type.price,
                "type_capacity": ap.type.capacity,
                "type_name": ap.type.name
            }
            result_apartments.append(ApartmentsResponse(**apartments_info))

        return result_apartments

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@apartment_routes.post("/booking", response_model=list[ApartmentsResponse])
async def apartment_booking(request: ApartmentsBookingRequest):
    try:

        for ap in request:
            reservation = Reservation()
            if reservation.depsrture_date < reservation.arrival_date:
                raise "Время отбытия должно быть больше времени прибытия"

            reservation.apartment_id = ap.id
            reservation.person_id = ap.person_id
            reservation.reserve_date = datetime.now()
            reservation.arrival_date = ap.start_date
            reservation.depsrture_date = ap.end_date

            helper.insert([reservation])
            helper.print_info()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@apartment_routes.post("/", response_model=list[ApartmentsResponse])
async def get_all_apartments_by_ids(request: ApartmentList):
    try:
        apartments = helper.get_apartments_by_ids(request.apartments)

        result_apartments = []
        for ap in apartments:
            apartments_info = {
                "id": ap.id,
                "number": ap.number,
                "hotel_name": ap.hotel.name,
                "hotel_city": ap.hotel.city,
                "cost": ap.type.price,
                "type_capacity": ap.type.capacity,
                "type_name": ap.type.name
            }
            result_apartments.append(ApartmentsResponse(**apartments_info))

        return result_apartments

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@apartment_routes.post("/availability", response_model=list[ApartmentAvailabilityResponse])
async def check_apartment_availability(request: ApartmentAvailabilityRequest):
    try:

        if request.end_date < request.start_date:
            raise "Время отбытия должно быть больше времени прибытия"

        apartments = helper.check_apartment_availability(request.start_date, request.end_date, request.id)

        result_apartments = []
        for ap in apartments:
            apartments_info = {
                "id": ap.id,
                "status": ap.status
            }
            result_apartments.append(ApartmentAvailabilityResponse(**apartments_info))

        return result_apartments

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))