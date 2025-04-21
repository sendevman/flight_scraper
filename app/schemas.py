from pydantic import BaseModel
from pydantic import ConfigDict

class FlightResponse(BaseModel):
    airline: str
    flight_number: str
    departure_date: str
    departure_airport: str
    arrival_airport: str
    status: str

    model_config = ConfigDict(from_attributes=True)