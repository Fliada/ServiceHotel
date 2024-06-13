from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()


class Reservation(Base):
    __tablename__ = __name__.lower()

    id =             Column(Integer, primary_key=True)
    apartment_id =   Column(Integer)
    person_id =      Column(Integer)
    cost =           Column(Integer)
    reserve_date =   Column(DateTime)
    arrival_date =   Column(DateTime)
    depsrture_date = Column(DateTime)

    # quantity = Column(Integer)  #кол-во товара в наличии
