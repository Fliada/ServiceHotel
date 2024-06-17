import uvicorn
from fastapi import FastAPI

from api.controller.apartment_controller import apartment_routes
from api.controller.hotel_controller import hotel_routes

app = FastAPI()
app.include_router(hotel_routes, prefix="/hotels", tags=["Hotel"])
app.include_router(apartment_routes, prefix="/apartments", tags=["Apartment"])


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
