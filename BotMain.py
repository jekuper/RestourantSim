from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from common import ThrottlingMiddleware

from handlers import greeting, store, profile, dayShift, taxCheck, brawlOrder, help, casino

from BotConfigs import USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE_NAME, TOKEN, COMMAND_LIMIT
import BotDataBase


dbEngine = BotDataBase.Connect()

bot = Bot(token=TOKEN, parse_mode="HTML")
#storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='gay')
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

dispatcher.middleware.setup(ThrottlingMiddleware(60 / COMMAND_LIMIT))

greeting.register_handlers(dispatcher)
store.register_handlers(dispatcher)
profile.register_handlers(dispatcher)
dayShift.register_handlers(dispatcher)
taxCheck.register_handlers(dispatcher)
brawlOrder.register_handlers(dispatcher)
help.register_handlers(dispatcher)
casino.register_handlers(dispatcher)

async def onShutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
if __name__ == '__main__':
    executor.start_polling(dispatcher, on_shutdown=onShutdown)