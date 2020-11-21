# for setup and test DB

from models import Item, User


def add_new_item():

    context = (12, 'Пластиковая бутылка', 15.9)

    plastic_bootle = Item().add_item(context)
    if plastic_bootle:
        print('Succses!')
    else:
        print('Failed')

add = User().add_points(1235)
if add:
    print('Succses')
else:
    print('Failed')
