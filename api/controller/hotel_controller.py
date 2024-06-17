from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends

from dao import hotel
from utils.schemas import *
from db_helper.DBHelper import DBHelper

hotel_routes = APIRouter()


@hotel_routes.get("/")
def read_root():
    return {"Hello": "World"}


@hotel_routes.post("/search_hotels", response_model=list[HotelResponse])
async def search_hotels(request: HotelRequest, helper: DBHelper = Depends()):
    try:
        available_hotels = helper.get_hotels_with_available_apartments(
            start_date=request.date,
            end_date=(
                    datetime.strptime(request.date, "%Y-%m-%d") + timedelta(days=2)
            ).strftime("%Y-%m-%d"),
            city=request.city,
        )

        filtered_hotels = []
        for hotel in available_hotels:
            hotel_info = {
                "id": hotel["id"],
                "name": hotel["name"],
                "location": {
                    "city": hotel["location"]["city"],
                    "street": hotel["location"]["street"],
                    "house_number": hotel["location"]["house_number"],
                },
                "min_cost": hotel["min_cost"],
                "max_cost": hotel["max_cost"],
            }
            filtered_hotels.append(HotelResponse(**hotel_info))

        return filtered_hotels

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@hotel_routes.post("/apartments", response_model=list[ApartmentsResponse])
async def get_apartments_by_ids(request: ApartmentList, helper: DBHelper = Depends()):
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
