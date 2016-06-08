from telegram_sender import *


class PythonListener(object):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, count=0):
        self.ROBOT_LIBRARY_LISTENER = self
        self.count = count
        self.stat = None

    def end_suite(self, name, attrs):
        self.stat = attrs['statistics']
        return self.stat

    def log_file(self, path):
        print self.stat
        test = Telegram()
        test.telegram_article(self.stat)
