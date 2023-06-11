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
    dpG.register_message_handler(process_brawl_order, lambda msg: BotLocalization.check_command_localization("brawl", msg, True) is not None, state=[None])
    
    if common.dp is None:
        common.dp = dpG

async def process_brawl_order(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    cost = 100

    if message.is_command() and message.get_args() is not None and message.get_args().isnumeric():
        cost = int(message.get_args())

    if message.reply_to_message is None:
        await message.reply(PHRASES["provide_reply"][user_language])
        return
    
    target_id = message.reply_to_message.from_id

    if BotDataBase.get_restourant(target_id) is None:
        await message.reply(PHRASES["user_not_exist"][user_language])
        return
    
    if BotDataBase.get_restourant(target_id).id == BotDataBase.get_restourant(message.from_id).id:
        await message.reply(PHRASES["brawl_self"][user_language])
        return

    if cost <= BotDataBase.get_balance(message.from_id):
        BotDataBase.change_balance(message.from_id, -cost)
        
        BotDataBase.change_brawl_damage(target_id, cost)
        await message.reply(PHRASES["brawl_level_increased"][user_language].format(name=BotDataBase.get_restourant(target_id).name))
    else:
        await message.reply(PHRASES["not_enough_balance"][user_language].format(price=str(cost)))
