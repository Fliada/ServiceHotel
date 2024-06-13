from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
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
                self.session.rollback()
                continue

    def print_info(self):
        products = self.session.query(Apartment).all()
        print(*products)

    def update(self, id, updates):
        item = self.session.query().filter_by(id=id).first()
        if item:
            for key, value in updates.items():
                setattr(item, key, value)
            self.session.commit()
        else:
            print("Запись не найдена")

    def delete(self, id):
        item = self.session.query(Apartment).filter_by(id=id).first()
        if item:
            self.session.delete(item)
            self.session.commit()
        else:
            print("Запись не найдена")

    def close(self):
        self.session.close()