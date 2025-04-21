# Flight Tracker API

## Setup

```bash
git clone <repo>
cd flight_scraper
python3 -m venv venv
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

http://127.0.0.1:8000/api/flight?airline_code=AA&flight_number=100&departure_date=2025-04-19%22