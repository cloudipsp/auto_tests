import telegram
from helper._settings import *
from telegram.ext import Updater


class Telegram(object):
    def __init__(self, token=None):
        self.token = token or default_token
        self.updater = None
        self.bot = None

    def update_bot(self):
        self.updater = Updater(token=self.token)
        self.bot = telegram.Bot(token=self.token)
        self.updater.start_polling()
        self.bot.getMe()
        self.bot.getUpdates()

    def telegram_article(self, status):
        self.update_bot()
        # chat_id = bot.getUpdates()[-1].message.chat_id  # add this string to update all telegram users
        chat_id = default_user
        self.bot.sendMessage(chat_id=chat_id, text=status)
        self.updater.stop()
