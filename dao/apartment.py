from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from dao import Type, Hotel
from dao import Base

class Apartment(Base):
    __tablename__ = "apartment"

    id =        Column(Integer, primary_key=True, autoincrement=True)
    hotel_id =  Column(Integer, ForeignKey('hotel.id'))
    number =    Column(Integer)
    type_id =   Column(Integer, ForeignKey('type.id'))

    type = relationship("Type")
    hotel = relationship("Hotel")