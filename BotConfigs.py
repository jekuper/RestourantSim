from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = "6000711537:AAH49O0PzDgnqMr9V8YKWfBr1dLT679R7nw"

class BotStates(StatesGroup):
    FIRST_LANGUAGE_SWITCH = State()
    LANGUAGE_SWITCH = State()
    SELECTING_NAME = State()

### data base

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "3i2fWRF8s_x5Cv_"
DATABASE_NAME = "restaurant_sim"