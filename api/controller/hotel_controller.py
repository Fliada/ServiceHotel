from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends

from db_helper.DBHelper import DBHelper 
from local_settings import postresql as settings
from utils.schemas import *

from config import helper

hotel_routes = APIRouter()


@hotel_routes.post("/search_hotels", response_model=list[HotelResponse])
async def search_hotels(request: HotelRequest):
    try:
        #print(request.city, request.capacity)

        available_hotels = helper.get_hotels_with_available_apartments(
            start_date=request.start_date,
            end_date=request.end_date,
            city=request.city,
            capacity=request.capacity,
            hotel_name=request.hotel_name, 
            type_name=request.type_name
        )

        if request.end_date < request.start_date:
            raise "Время отбытия должно быть больше времени прибытия"

        filtered_hotels = []
        for hotel in available_hotels:
            filtered_hotels.append(HotelResponse(**hotel))

        return filtered_hotels

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

