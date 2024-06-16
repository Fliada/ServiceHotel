import uvicorn
from fastapi import FastAPI

from api.controller.hotel_controller import hotel_routes
from db_helper.DBHelper import *
from local_settings import postresql as settings

app = FastAPI()
app.include_router(hotel_routes, prefix="/hotel", tags=["Hotel"])

keys = ["pguser", "pgpasswd", "pghost", "pgport", "pgdb"]
if not all(key in keys for key in settings.keys()):
    raise Exception("Bad confid file")

helper = DBHelper(
    settings["pguser"],
    settings["pgpasswd"],
    settings["pghost"],
    settings["pgport"],
    settings["pgdb"],
)


def main():
    helper.create_table()


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
    main()
