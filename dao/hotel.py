from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from dao import Base


class Hotel(Base):
    __tablename__ = "hotel"

    id =            Column(Integer, primary_key=True, autoincrement=True)
    name =          Column(String)
    city =          Column(String)
    street =        Column(String)
    house_number =  Column(Integer)