from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Apartment(Base):
    __tablename__ = __name__.lower()

    id =        Column(Integer, primary_key=True)
    hotel_id =  Column(Integer)
    number =    Column(Integer)
    type_id =   Column(Integer)
    status_id = Column(Integer)