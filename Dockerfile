FROM python:3.11

WORKDIR ServiceHotel

COPY . ./app/hotel_service

RUN apt-get update && apt-get install
RUN pip install -r ./app/hotel_service/requirements.txt

EXPOSE 8000

CMD ["python", "-O", "./app/hotel_service/main.py"]
