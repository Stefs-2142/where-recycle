import logging
import telegram
from telegram.utils.request import Request


from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters)

from settings import TELEGRAM_API_KEY

from handlers import greet_user, users_coordinates

logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',)


def main():

    request = Request(con_pool_size=8)
    bot = telegram.Bot(TELEGRAM_API_KEY, request=request)

    wr_bot = Updater(bot=bot, use_context=True)

    dp = wr_bot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("location", users_coordinates))

    logging.info('Бот стартовал')

    wr_bot.start_polling()
    wr_bot.idle()


if __name__ == "__main__":
    main()
