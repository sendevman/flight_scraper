from sqlalchemy import Column, Integer, String
from .database import Base

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String)
    flight_number = Column(String)
    departure_date = Column(String)
    departure_airport = Column(String)
    arrival_airport = Column(String)
    status = Column(String)