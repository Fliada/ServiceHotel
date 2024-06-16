from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException

from utils.schemas import HotelRequest, HotelResponse

hotel_routes = APIRouter()


@hotel_routes.get("/")
def read_root():
    return {"Hello": "World"}


@hotel_routes.post("/search_hotels", response_model=list[HotelResponse])
async def search_hotels(request: HotelRequest, helper):
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
