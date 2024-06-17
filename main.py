import uvicorn
from fastapi import FastAPI

from api.controller.hotel_controller import hotel_routes

app = FastAPI()
app.include_router(hotel_routes, prefix="/hotel", tags=["Hotel"])


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
