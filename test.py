from local_settings import postresql as settings
from dao import Reservation, Hotel
from db_helper.DBHelper import *
from datetime import datetime

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

def add_hotels(hotels: list[Hotel]):
    helper.insert(hotels)
    pass

def main():
    reservation = Reservation()
    reservation.apartment_id = 1
    reservation.person_id = 4
    reservation.reserve_date = datetime.now()
    reservation.arrival_date = datetime(2024, 7, 7, 14, 0)
    reservation.depsrture_date = datetime(2024, 7, 8, 11, 0)

    if reservation.depsrture_date < reservation.arrival_date:
        raise "Время отбытия должно быть больше времени прибытия"

    filename = "C:\\Users\\zxc ghoul\\Downloads\\отели\\Отели.txt"

    hotels = []
    with open(filename,encoding='utf-8') as file:
        for line in file:
            hotel = Hotel()
            col = line.replace('\n', '').split(',')

            if col[0] == 'name': continue

            hotel.name=col[0]
            hotel.city=col[1]
            hotel.street=col[2]
            hotel.house_number=col[3]

            hotels.append(hotel)

            helper.insert([hotel])


    # add_hotels(hotels)
    
    # helper.insert([reservation])  # Обратите внимание, что insert ожидает список
    # helper.print_info()

    # start_date = datetime(2024, 7, 10)
    # end_date = datetime(2024, 7, 16)
    # available_apartments = helper.get_available_apartments(start_date, end_date, capacity=2)
    # for apartment in available_apartments:
    #     print(apartment.id, apartment.type.capacity, apartment.hotel)

    # start_date = datetime(2024, 7, 8)
    # end_date = datetime(2024, 7, 16)
    # apartment_ids = [1, 4, 2]

    # apartments=[
    #     {
    #         "id": 1,
    #         "start_date": datetime(2024, 7, 8),
    #         "end_date":datetime(2024, 7, 16)
    #     },
    #     {
    #         "id": 4,
    #         "start_date": datetime(2024, 7, 8),
    #         "end_date":datetime(2024, 7, 16)
    #     }
    # ]
    # availability_status = helper.check_apartment_availability(apartments=apartments)
    # for status in availability_status:
    #     print(f"Apartment ID: {status['id']}, Status: {status['status']}")

    # apartment_ids = [1, 2, 4]  # Пример списка id квартир

    # apartments = helper.get_apartments_by_ids(apartment_ids)
    # for apartment in apartments:
    #     print(apartment.id, apartment.number, apartment.type.name)

    # start_date = datetime(2024, 7, 18, 14, 0)
    # end_date = datetime(2024, 7, 21, 11, 0)

    # city = 'Москва'

    # hotels = helper.get_hotels_with_available_apartments(start_date, end_date, city)
    # print(*hotels, sep='\n')


if __name__ == '__main__':
    main()