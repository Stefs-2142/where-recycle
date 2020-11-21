from collections import namedtuple

import sqlalchemy.exc
from base import session, Base, Engine
from sqlalchemy import (
    exists, Column,
    BigInteger, Boolean, Integer, Text, Date, Float
)


class User(Base):
    __tablename__ = 'users'

    user_id = Column('user_id', BigInteger, primary_key=True)
    green_points = Column('green_points', Float)
    green_tickets = Column('green_tickets', Integer)

    def add_user(self, user_id):
        """
        Добавляем пользователя в БД.
        """
        candidate_user = User(
            user_id=user_id,
            green_points=0,
            green_tickets=0
        )
        session.add(candidate_user)
        try:
            session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            return False

    def add_points(self, item_id):
        """
        Дабавляем бонусы за переработку/утилизация.
        """
        item_green_point = 12.5
        User.green_points += item_green_point
        try:
            session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            return False

    def get_balance(self, query_user_id):
        """
        Получаем из БД данные о баллах и доступных билетах.
        """
        user_balance = session.query(User).filter(User.user_id == query_user_id).all()
        packed_balance = []
        for elem in user_balance:
            packed_balance.append([
                elem.green_points,
                elem.green_tickets

            ])
        return packed_balance


class Recycle_point(Base):
    __tablename__ = 'recycle_points'

    recycle_point_id = Column('recycle_point_id', BigInteger, primary_key=True)
    point_type = Column('point_type', Text)
    location = Column('location', Text)


class Green_ticket(Base):
    __tablename__ = 'green_tickets'

    green_ticket_id = Column('green_ticket_id', BigInteger, primary_key=True)
    ticket_type = Column('ticket_type', Text)
    point_cost = Column('point_cost', Float)


class Item(Base):
    __tablename__ = 'items'

    item_id = Column('items_id', BigInteger, primary_key=True)
    item_type = Column('items_type', Text)
    green_points = Column('green_points', Float)

    def add_item(self, item_data):
        '''
        Метод позволяющий добавлять утилизируемые/перерабатываемые
        предметы/вещи.
        '''

        (
            item_id_cand, item_type_cand,
            green_points_cand
        ) = item_data

        Item_data = namedtuple('Item_data', 'item_id item_type gree_points')
        i_d = Item_data(item_id_cand, item_type_cand, green_points_cand)

        candidate_item = Item(
            item_id=i_d[0],
            item_type=i_d[1],
            green_points=i_d[2],
        )
        session.add(candidate_item)

        try:
            session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            session.rollback()
            return False



