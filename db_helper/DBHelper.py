from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from dao import *


class DBHelper:
    def __init__(self, user, passwd, host, port, db):
        postgresql_url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
        print(postgresql_url)
        if not database_exists(postgresql_url):
            create_database(postgresql_url)
        self.engine = create_engine(postgresql_url)
        self.session = sessionmaker(bind=self.engine)()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def insert(self, data):
        for product in data:
            self.session.add(product)
            try:
                self.session.commit()
            except IntegrityError as e:
                print(e)
                self.session.rollback()
                continue

    def print_info(self):
        products = self.session.query(Reservation).all()
        print(*products, sep='\n')

    def update(self, id, updates):
        item = self.session.query().filter_by(id=id).first()
        if item:
            for key, value in updates.items():
                setattr(item, key, value)
            self.session.commit()
        else:
            print("Запись не найдена")

    def delete(self, id):
        item = self.session.query(Reservation).filter_by(id=id).first()
        if item:
            self.session.delete(item)
            self.session.commit()
        else:
            print("Запись не найдена")

    def close(self):
        self.session.close()

    def get_available_apartments(self, start_date, end_date, city=None, capacity=None, hotel_name=None, type_name=None):
        # Создаем базовый запрос для поиска апартаментов
        query = self.session.query(Apartment).join(Apartment.type).join(Apartment.hotel).options(
            joinedload(Apartment.type), 
            joinedload(Apartment.hotel)
        )

        # Применяем фильтры, если они заданы
        if city:
            query = query.filter(Hotel.city == city)
        if capacity:
            query = query.filter(Type.capacity == capacity)
        if hotel_name:
            query = query.filter(Hotel.name == hotel_name)
        if type_name:
            query = query.filter(Type.name == type_name)

        # Находим занятые апартаменты в заданный период
        subquery = self.session.query(Reservation.apartment_id).filter(
            and_(
                Reservation.arrival_date < end_date,
                Reservation.depsrture_date > start_date
            )
        ).subquery()

        # Исключаем занятые апартаменты из основного запроса
        query = query.filter(Apartment.id.notin_(subquery))

        # Выполняем запрос и возвращаем результат
        available_apartments = query.all()
        return available_apartments
    
    def check_apartment_availability(self, start_date, end_date, apartment_ids):
        availability = []

        for apartment_id in apartment_ids:
            # Подзапрос для поиска пересекающихся бронирований
            overlapping_reservations = self.session.query(Reservation).filter(
                and_(
                    Reservation.apartment_id == apartment_id,
                    Reservation.arrival_date < end_date,
                    Reservation.depsrture_date > start_date
                )
            ).all()

            # Определение статуса доступности
            if overlapping_reservations:
                availability.append({'apartment_id': apartment_id, 'status': False})
            else:
                availability.append({'apartment_id': apartment_id, 'status': True})

        return availability
    
    
    def get_apartments_by_ids(self, apartment_ids):
        apartments = self.session.query(Apartment).filter(Apartment.id.in_(apartment_ids)).all()
        return apartments