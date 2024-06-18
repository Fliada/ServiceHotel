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


@apartment_routes.post("/booking")
async def apartment_booking(request: ApartmentBookingList):
    try:        
        reservations = []
        for ap in request.apartments:
            reservation = Reservation()

            reservation.apartment_id = ap.id
            reservation.person_id = ap.person_id
            reservation.reserve_date = datetime.now()
            reservation.arrival_date = ap.start_date
            reservation.depsrture_date = ap.end_date

            reservations.append(reservation)
            print(ap)

        helper.insert(reservations)

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


@apartment_routes.post("/availability", response_model=ApartmentAvailabilityResponseList)
async def check_apartment_availability(request: ApartmentAvailabilityList):
    try:
        apartments = helper.check_apartment_availability(request.apartments)

        result_apartments = []
        for ap in apartments:
            result_apartments.append(ApartmentAvailabilityResponse(**ap))

        return {
            "user_id": request.user_id,
            "order_id": request.order_id,
            "apartments": result_apartments
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))