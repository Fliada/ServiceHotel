from pydantic import BaseModel
from typing import List
from datetime import date
class HotelResponse(BaseModel):
    name: str
    location: str
    start_date: date
    end_date: date
    price: int

class HotelsResponse(BaseModel):
    hotels: List[HotelResponse]

class HotelRequest(BaseModel):
    city: str
    date: date