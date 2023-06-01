from aiogram.dispatcher import Dispatcher
from aiogram import types
import BotLocalization
from BotConfigs import BotStates
import BotDataBase
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import handlers.common as common
from BotLocalization import COMMANDS, PHRASES

def register_handlers(dpG: Dispatcher):
    dpG.register_message_handler(process_check, lambda msg: BotLocalization.check_command_localization("tax_check", msg) is not None, state=[None])
    
    if common.dp is None:
        common.dp = dpG

async def process_check(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    cost = BotDataBase.get_income(message.from_id) * 3

    if message.reply_to_message is None:
        await message.reply(PHRASES["provide_reply"][user_language])
        return
    
    target_id = message.reply_to_message.from_id

    if BotDataBase.get_restourant(target_id) is None:
        await message.reply(PHRASES["user_not_exist"][user_language])
        return

    if cost <= BotDataBase.get_balance(message.from_id):
        BotDataBase.change_balance(message.from_id, -cost)
        debt = BotDataBase.get_total_debt(target_id)
        BotDataBase.change_balance(target_id, -debt)
        BotDataBase.nullify_debt(target_id)
        await message.bot.send_message(target_id, PHRASES["tax_skipped_fail"][BotDataBase.get_user_language(target_id)].format(fine=debt))
        await message.reply(PHRASES["tax_check_sent"][user_language].format(name=BotDataBase.get_restourant(message.from_id).name))
    else:
        await message.reply(PHRASES["not_enough_balance"][user_language].format(price=str(cost)))
