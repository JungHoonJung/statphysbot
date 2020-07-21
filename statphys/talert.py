from .bot import bot
from .auth import auth_user
import sys, os
import datetime as dt
from io import StringIO

__all__ = ['talert']

def running_with_talert(bash_command):
    pass

name, target_id = auth_user()

class talertBase:
    """simple telegram alert machine."""

    def __init__(self, bot, target):
        self.bot = bot
        self.name = None

    def __enter__(self):
        self.stdout = StringIO()
        self.old = sys.stdout
        sys.stdout = self.stdout
        self.start_time = dt.datetime.now()

    def __exit__(self, type, val, trace):
        self.stdout.seek(0)
        stdout = self.stdout.readlines()
        sys.stdout = self.old
        for text in stdout:
            sys.stdout.write(text)

        work_name = '작업' if self.name is None else f"'{self.name}' 작업"

        if type is not None:
            stdout.insert(0, "{}중에 에러가 발생하였습니다.\r\n".format(work_name))
            stdout.append('에러 발생 코드를 확인해주세요\r\n')
        else:
            stdout.insert(0, "{}이 완료되었습니다.\r\n".format(work_name))

        text = ''
        for line in stdout:
            text+=line

        total_time = dt.datetime.now()-self.start_time


        self.bot.send_message(chat_id = self.target, text = text)

    def __call__(self, work_name = None):
        self.name = work_name
        return self

talert = talertBase(bot, target_id)
