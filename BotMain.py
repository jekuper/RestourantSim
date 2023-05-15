from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from handlers import greeting

from BotConfigs import TOKEN
from BotDataBase import *

bot = Bot(token=TOKEN, parse_mode="HTML")
#storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='gay')
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

dispatcher.middleware.setup(LoggingMiddleware())

greeting.register_handlers_greeting(dispatcher)

async def onShutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
if __name__ == '__main__':
    executor.start_polling(dispatcher, on_shutdown=onShutdown)