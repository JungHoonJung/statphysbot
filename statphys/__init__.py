from .auth import auth_user

__version__ = 0.1

name, target_id = auth_user()

from .bot import bot
from .talert import *
