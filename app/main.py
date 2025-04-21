from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, scraper
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/flight", response_model=schemas.FlightResponse)
def get_flight_data(
    airline_code: str = Query(...),
    flight_number: str = Query(...),
    departure_date: str = Query(...),
    db: Session = Depends(get_db)
):
    try:
        data = scraper.scrape_flight_data(airline_code, flight_number, departure_date)
        flight = models.Flight(**data)
        db.add(flight)
        db.commit()
        db.refresh(flight)
        return flight
    except Exception as e:
        print(" Error occurred:", e)
        raise HTTPException(status_code=500, detail=str(e))