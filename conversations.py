from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler

from handlers import choice_type, get_location, get_route, operation_cancel


point = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^Найти пункт ♻️'), choice_type)],
    states={
        '1': [
            MessageHandler(
                Filters.text & (~Filters.regex('^(Отмена|Назад)$')), get_location
            ),
        ],
        '2': [
            MessageHandler(
                Filters.location & (~Filters.regex('^(Отмена|Назад)$')), get_route
            )
        ]
    },
    fallbacks=[
        MessageHandler(Filters.regex('^(Отмена)$'), operation_cancel),
    ]
)
