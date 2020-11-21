from telegram import ParseMode
from keyboards import main_menu_keyboard


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


def get_location(update, context):

    location = update.message.location
    update.message.reply_text(f'Caught you! {location}')

    context.user_data['user_id'] = [update.effective_user.id]
    context.user_data['location'] = [update.message.location]
