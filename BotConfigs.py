from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = "6000711537:AAH49O0PzDgnqMr9V8YKWfBr1dLT679R7nw"

class BotStates(StatesGroup):
    FIRST_LANGUAGE_SWITCH = State()
    LANGUAGE_SWITCH = State()
    SELECTING_NAME = State()
    FIRST_WORKER = State()
    COMPLETING_DEAL = State()

### data base

HOSTNAME = "127.0.0.1"
PORT = 0
USERNAME = "dsharipov"
PASSWORD = "WU6qk85eLWFS6*P"
DATABASE_NAME = "dsharipov"
