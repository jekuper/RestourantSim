from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from handlers import greeting, store

from BotConfigs import USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE_NAME, TOKEN
import BotDataBase


dbEngine = BotDataBase.Connect()

bot = Bot(token=TOKEN, parse_mode="HTML")
#storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='gay')
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

dispatcher.middleware.setup(LoggingMiddleware())

greeting.register_handlers(dispatcher)
store.register_handlers(dispatcher)

async def onShutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
if __name__ == '__main__':
    executor.start_polling(dispatcher, on_shutdown=onShutdown)