import requests
from bs4 import BeautifulSoup

def scrape_flight_data(airline_code, flight_number, departure_date):
    search_url = "https://www.flightstats.com/v2/flight-tracker/search"
    
    params = {"query": f"{airline_code} {flight_number}"}
    response = requests.get(search_url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")


    flight_info = {
        "airline": airline_code,
        "flight_number": flight_number,
        "departure_date": departure_date,
        "departure_airport": "Extracted...",
        "arrival_airport": "Extracted...",
        "status": "Extracted...",
    }
    return flight_info