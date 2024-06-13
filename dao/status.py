from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Status(Base):
    __tablename__ = __name__.lower()

    id =    Column(Integer, primary_key=True)
    name =  Column(String)
    # reserved = 1
    # free = 2
    # occupied = 3