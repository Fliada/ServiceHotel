from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class HotelResponse(BaseModel):
    name: str
    location: str
    start_date: date
    end_date: date
    price: int


class HotelsResponse(BaseModel):
    hotels: List[HotelResponse]
    min_price: Optional[int] = None
    max_price: Optional[int] = None


class HotelRequest(BaseModel):
    city: str
    date: date
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None


class ApartmentsResponse(BaseModel):
    id: int
    number: int
    hotel_name: str
    hotel_city: str
    cost: int
    type_capacity: int
    type_name: str


class ApartmentList(BaseModel):
    apartments: list[int] = []
