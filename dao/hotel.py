from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Hotel(Base):
    __tablename__ = __name__.lower()

    id =            Column(Integer, primary_key=True)
    name =          Column(String)
    city =          Column(String)
    street =        Column(String)
    house_number =  Column(Integer)
    # quantity = Column(Integer)  #кол-во товара в наличии
