import sqlalchemy.exc
from .base import session, Base
from sqlalchemy import (
    exists, Column,
    BigInteger, Boolean, Integer, Text, Date, Float
)


class User(Base):
    __tablename__ = 'users'

    user_id = Column('user_id', BigInteger, primary_key=True)
    green_points = Column('green_ponts', Float)
    green_tickets = Column('green_tickets', Integer)

    def __repr__(self):
        return f'<User {self.user_id} have:{self.green_points} and {self.green_tickets}'


class Recycle_point(Base):
    __tablename__ = 'recycle_points'

    recycle_point_id = Column('recycle_point_id', BigInteger, primary_key=True)
    point_type = Column('point_type', Text)
    location = Column('location', Text)

    def __repr__(self):
        repr_msg = f'<Recycle point {self.recycle_point_id} type:{self.point_type} \
        loc:{self.location}'
        return repr_msg


class Green_ticket(Base):
    __tablename__ = 'green_tickes'

    user_id = Column('user_id', BigInteger, primary_key=True)
    green_points = Column('green_ponts', Float)
    green_tickets = Column('green_tickets', Integer)

    def __repr__(self):
        return f'<User {self.user_id} have:{self.green_points} and {self.green_tickets}'


class Recycle_point(Base):
    __tablename__ = 'recycle_points'

    user_id = Column('user_id', BigInteger, primary_key=True)
    green_points = Column('green_ponts', Float)
    green_tickets = Column('green_tickets', Integer)

    def __repr__(self):
        return f'<User {self.user_id} have:{self.green_points} and {self.green_tickets}'

