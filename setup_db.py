# for setup and test DB

from models import Item, User, Recycle_point
from base import session


def add_new_item():

    context = (12, 'Пластиковая бутылка', 15.9)

    plastic_bootle = Item().add_item(context)
    if plastic_bootle:
        print('Succses!')
    else:
        print('Failed')


def add_point():
    add = User().add_points(322)
    if add:
        print('Succses')
    else:
        print('Failed')


def new_user():
    new_user = User().add_user(25789)
    if new_user:
        print('Succses')
    else:
        print('Failed')

def get_balance(query_user_id):
    user_balance = User().get_balance(query_user_id)
    if user_balance:
        print(user_balance)

# new_user()

#get_balance(25789)


new_point = Recycle_point(
    recycle_point_id=3094,
    point_type='paper',
    location='59.9459608967471 30.2163229080734')

new_point_1 = Recycle_point(
    recycle_point_id=22873,
    point_type='paper',
    location='59.95005984843247 30.24613587853173')

session.add(new_point)
session.add(new_point_1)
session.commit()
