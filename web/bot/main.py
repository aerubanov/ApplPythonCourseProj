from tokens import TELEGRAM_TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import handlers
from logger import logger


class Bot:
    # handlers
    start_handler = CommandHandler('start', handlers.start)
    photo_handler = MessageHandler(Filters.photo, handlers.photo)
    unknown_handler = MessageHandler(Filters.command, handlers.unknown)
    wolfram_handler = MessageHandler(Filters.regex('^(Продолжить)$'), handlers.wolfram_request)
    retry_handler = MessageHandler(Filters.regex('^(Вернуться назад)$'), handlers.retry)
    correction_handler = MessageHandler(Filters.regex('^(Предложить исправление)$'), handlers.correction)
    correct_label_handler = MessageHandler(Filters.regex('^(/[0-9]+/\s\w+)$'), handlers.correct_labels)

    def __init__(self):
        print(TELEGRAM_TOKEN)
        self.updater = Updater(TELEGRAM_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(self.start_handler)
        self.dispatcher.add_handler(self.photo_handler)
        self.dispatcher.add_handler(self.unknown_handler)
        self.dispatcher.add_handler(self.wolfram_handler)
        self.dispatcher.add_handler(self.retry_handler)
        self.dispatcher.add_handler(self.correction_handler)
        self.dispatcher.add_handler(self.correct_label_handler)

    def start(self):
        self.updater.start_polling()
        logger.info('Bot running')


if __name__ == "__main__":
    b = Bot()
    b.start()
