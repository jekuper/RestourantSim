from aiogram.dispatcher import Dispatcher
from aiogram import types
import BotLocalization
import BotDataBase
from aiogram.dispatcher import FSMContext
import handlers.common as common
import json

def register_handlers(dpG: Dispatcher):
    dpG.register_message_handler(process_profile, lambda msg: BotLocalization.check_command_localization("profile", msg) is not None, state=None)

    if common.dp is None:
        common.dp = dpG

async def process_profile(message: types.Message, state: FSMContext):
    result = ""
    property = BotDataBase.get_property(message.from_id)
    rest = BotDataBase.get_restourant(message.from_id)
    result += "balance = " + str(property.balance) + "\n"
    result += "workers = " + rest.workers + "\n"
    result += "income = " + str(rest.income) + "\n"
    await message.reply(result)