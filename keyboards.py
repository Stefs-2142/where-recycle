from telegram import ReplyKeyboardMarkup, KeyboardButton


def location_button(update, context):
    return KeyboardButton(
        text='Найти пункт ♻️',
        request_location=True,
        )


def main_menu_keyboard(update, context):
    return ReplyKeyboardMarkup([
        [location_button(), 'Моя статистика 📝']
    ], row_width=1, resize_keyboard=True)
