from telegram import ReplyKeyboardMarkup, KeyboardButton

TRASH_TYPES = ['🥤', '📚', '👖', '🔋']


def location_button():
    return KeyboardButton(
        text="Поделиться локацией 📍",
        request_location=True,
        )


def location_keyboard():
    return ReplyKeyboardMarkup([
        [location_button()]
    ], row_width=1, resize_keyboard=True,
        one_time_keyboard=True)


def location_and_cancel_keyboard():
    return ReplyKeyboardMarkup([
        [location_button()],
        ['Отмена']
    ], row_width=1, resize_keyboard=True)


def choice_keyboard():
    return ReplyKeyboardMarkup([
        ['🥤', '📚', '👖', '🔋']
    ], row_width=1, resize_keyboard=True)


def main_menu_keyboard():
    return ReplyKeyboardMarkup([
        ['Найти пункт ♻️', 'Мои баллы 📝']
    ], row_width=1, resize_keyboard=True)


def cancel_keyboard():
    return ReplyKeyboardMarkup([
        ['Отмена']
    ])
