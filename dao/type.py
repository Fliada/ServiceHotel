from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Double
from dao import Base


class Type(Base):
    __tablename__ = "type"

    id =        Column(Integer, primary_key=True, autoincrement=True)
    name =      Column(String)
    capacity =  Column(Integer)
    price =     Column(Double)