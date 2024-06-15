from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from dao import Apartment
from dao import Base


class Reservation(Base):
    __tablename__ = "reservation"

    id =             Column(Integer, primary_key=True, autoincrement=True)
    apartment_id =   Column(Integer, ForeignKey('apartment.id'))
    person_id =      Column(Integer)
    cost =           Column(Integer)
    reserve_date =   Column(DateTime)
    arrival_date =   Column(DateTime)
    depsrture_date = Column(DateTime)

    apartment = relationship("Apartment")