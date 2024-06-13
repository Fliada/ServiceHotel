from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Double

Base = declarative_base()


class Type(Base):
    __tablename__ = __name__.lower()

    id =        Column(Integer, primary_key=True)
    name =      Column(String)
    capacity =  Column(Integer)
    price =     Column(Double)