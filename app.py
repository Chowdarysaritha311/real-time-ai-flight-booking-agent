from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import uvicorn
from datetime import datetime, timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FlightRequest(BaseModel):
    from_city: str
    to_city: str
    date: str
    travelers: int

airlines = ["Air India", "IndiGo", "SpiceJet", "Vistara", "GoAir"]

@app.post("/search_flights")
def search_flights(request: FlightRequest):
    flights = []
    for _ in range(5):
        airline = random.choice(airlines)
        dep_time = datetime.strptime(request.date, "%Y-%m-%d") + timedelta(hours=random.randint(5, 20))
        arr_time = dep_time + timedelta(hours=random.randint(1, 5))
        duration = arr_time - dep_time
        price = random.randint(4000, 15000)
        flight_number = airline[:2].upper() + str(random.randint(100, 999))
        seats_available = random.randint(5, 50)
        flights.append({
            "flight_number": flight_number,
            "airline": airline,
            "from": request.from_city,
            "to": request.to_city,
            "departure": dep_time.strftime("%H:%M"),
            "arrival": arr_time.strftime("%H:%M"),
            "duration": f"{duration.seconds//3600}h {(duration.seconds//60)%60}m",
            "price": price,
            "seats_available": seats_available
        })
    flights.sort(key=lambda x: x["price"])
    return {"flights": flights}

@app.post("/book_flight")
def book_flight(flight: dict):
    booking_id = random.randint(1000, 9999)
    return {
        "message": "Booking Confirmed!",
        "booking_id": booking_id,
        "flight_details": flight
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
