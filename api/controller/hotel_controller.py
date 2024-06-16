from fastapi import HTTPException, APIRouter
from utils.schemas import HotelsResponse, HotelRequest
import httpx

hotel_routes = APIRouter()


@hotel_routes.get("/")
def read_root():
    return {"Hello": "World"}


@hotel_routes.post("/search_hotels", response_model=HotelsResponse)
async def search_hotels(request: HotelRequest):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "URL_СЕРВИСА_ОТЕЛЕЙ",
                json={"city": request.city, "date": request.date}
            )
            response.raise_for_status()
            hotels_data = response.json()
            return HotelsResponse(hotels=hotels_data["hotels"])
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
