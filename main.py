from local_settings import postresql as settings
from db_helper.DBHelper import *
from fastapi import FastAPI, HTTPException
from utils.schemas import HotelsResponse, HotelRequest
import httpx

app = FastAPI()
keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
if not all(key in keys for key in settings.keys()):
    raise Exception('Bad confid file')

helper = DBHelper(
    settings['pguser'],
    settings['pgpasswd'],
    settings['pghost'],
    settings['pgport'],
    settings['pgdb']
)

def main():
    helper.create_table()


if __name__ == '__main__':
    main()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/search_hotels", response_model=HotelsResponse)
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
            raise   HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))