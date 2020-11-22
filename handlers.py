from telegram import ParseMode
from telegram.ext import ConversationHandler

from keyboards import main_menu_keyboard, choice_keyboard, location_and_cancel_keyboard
from keyboards import TRASH_TYPES, cancel_keyboard, location_keyboard

from models import User


def greet_user(update, context):

    try:
        name = update.effective_user['first_name']
    except KeyError:
        name = update.effective_user['username']

    update.message.reply_text(
        f"""Привет <b>{name}</b>! \n
    Ты можешь найти ближайший пукнт для переработки.
    Или проверить свои бонусы в личном кабинете.""",
        reply_markup=main_menu_keyboard(),
        parse_mode=ParseMode.HTML)


def choice_type(update, context):
    """Запрашиваем у пользователя тип объекта"""
    update.message.reply_text(
        "Что ты хочешь сдать?", reply_markup=choice_keyboard())
    return '1'


def get_location(update, context):
    """
    Если выбран валидный тип продолжаем.
    Добавляем юзера в БД, если ранее не было.
    """

    text = update.message.text
    if text in TRASH_TYPES:
        update.message.reply_text(
            'Сейчас покажу что рядом. Только мне нужно узнать где ты находишся.',
            reply_markup=location_keyboard())

        user_id = update.effective_user.id
        user_id = User().add_user(user_id)
        return '2'
    else:
        update.message.reply_text(
            """
            Если Вашей категории нет - обратитесь пожалуйста к админам.\n
            https://t.me/Stefs""", reply_markup=main_menu_keyboard())
        return ConversationHandler.END


def get_route(update, context):
    """
    Записываем локацию юзера
    """
    location = update.message.location
    if location is not None:
        context.user_data['location'] = update.message.location
        update.message.reply_text(f'Caught you! {location}', reply_markup=main_menu_keyboard())
        return ConversationHandler.END
    else:
        update.message.reply_text(
            'Без локации мы не сможешь Вам помочь. Попробуй ещё раз или нажми "Отмена"',
            reply_markup=location_and_cancel_keyboard())
        return '2'


def unknown_text(update, context):
    """
    Функция, обрабатывающая любой текст, который не является текстом из
    кнопок, которые начинают Conversation
    """
    reply = ("Выберите доступный раздел.")
    update.message.reply_text(reply, reply_markup=main_menu_keyboard())


def operation_cancel(update, context):
    """
    Функция fallback команды "Отмена" - удаляет данные из контекстов и
    завершает текущий Conversation
    """
    context.user_data.pop('location', None)

    update.message.reply_text(
        'Операция прервана', reply_markup=main_menu_keyboard()
    )
    return ConversationHandler.END


def test_inline(update, context):

    update.message.reply_text(
        'test', reply_markup=choice_keyboard())


def get_my_stat(update, context):

    user_id = update.effective_user.id
    User().add_user(user_id)
    user_data = User().get_balance(user_id)

    message = 'На Вашем счету:\n'
    for data in user_data:
        message += f'Green Points-{data[0]}\n'
        message += f'Green Tickets-{data[1]}'
    update.message.reply_text(
        message, reply_markup=main_menu_keyboard()
        )
