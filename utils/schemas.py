from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class HotelResponse(BaseModel):
    id: int
    name: str
    location: dict
    min_cost: int
    max_cost: int


class HotelsResponse(BaseModel):
    hotels: List[HotelResponse]
    min_price: Optional[int] = None
    max_price: Optional[int] = None


class HotelRequest(BaseModel):
    city: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    capacity: Optional[int] = None
    hotel_name: Optional[str] = None
    type_name: Optional[str] = None


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


class AvailableApartmentsRequest(BaseModel):
    start_date: datetime
    end_date: datetime
    city: Optional[str] = None
    capacity: Optional[int] = None
    hotel_name: Optional[str] = None
    type_name: Optional[str] = None


class ApartmentsBookingRequest(BaseModel):
    id: int
    person_id: int
    start_date: datetime
    end_date: datetime

class ApartmentBookingList(BaseModel):
    apartments: list[ApartmentsBookingRequest]


class ApartmentAvailabilityRequest(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime

class ApartmentAvailabilityResponse(BaseModel):
    id: int
    status: bool

class ApartmentAvailabilityList(BaseModel):
    user_id: int
    order_id: int
    apartments: list[ApartmentAvailabilityRequest]


class ApartmentAvailabilityResponseList(BaseModel):
    user_id: int
    order_id: int
    apartments: list[ApartmentAvailabilityResponse]