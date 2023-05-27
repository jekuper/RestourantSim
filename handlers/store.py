from aiogram.dispatcher import Dispatcher
from aiogram import types
import BotLocalization
from BotConfigs import BotStates
import BotDataBase
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import handlers.common as common
from BotLocalization import COMMANDS, PHRASES

def register_handlers(dpG: Dispatcher):
    dpG.register_message_handler(process_category, lambda msg: BotLocalization.check_command_localization("employment", msg) is not None, state=[BotStates.FIRST_WORKER, None])
    dpG.register_message_handler(process_chiefs_store, lambda msg: BotLocalization.check_command_localization("chiefs", msg) is not None, state=[None])
    dpG.register_message_handler(process_servant_store, lambda msg: BotLocalization.check_command_localization("servants", msg) is not None, state=[None])

    if common.dp is None:
        common.dp = dpG

async def process_category(message: types.Message, state: FSMContext):
    await state.reset_state()

    categorySelection = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_language = BotDataBase.get_user_language(message.from_id)
    
    chiefs_button = KeyboardButton(COMMANDS["chiefs"][user_language])
    servants_button = KeyboardButton(COMMANDS["servants"][user_language])
    categorySelection.add(chiefs_button)
    categorySelection.add(servants_button)

    await message.reply(PHRASES["storeCategory"][user_language], reply_markup=categorySelection)

async def process_servant_store(message: types.Message, state: FSMContext):
    servantsList = ReplyKeyboardMarkup(resize_keyboard=True)
    user_language = BotDataBase.get_user_language(message.from_id)
    
    available_deals = BotDataBase.get_available_human_deals(message.from_id, BotDataBase.job_types.servant)

    for i in range(1, len(available_deals), 2):
        servantsList.add(KeyboardButton(available_deals[i - 1].last_name+" "+available_deals[i - 1].name+"\n"+str(available_deals[i - 1].income)),
                         KeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income)))
    if len(available_deals) % 2 != 0:
        i = len(available_deals) - 1
        servantsList.add(KeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income)))
    
    await message.reply(PHRASES["selectServantStore"][user_language], reply_markup=servantsList)

async def process_chiefs_store(message: types.Message, state: FSMContext):
    chiefsList = ReplyKeyboardMarkup(resize_keyboard=True)
    user_language = BotDataBase.get_user_language(message.from_id)
    
    available_deals = BotDataBase.get_available_human_deals(message.from_id, BotDataBase.job_types.chief)

    for i in range(1, len(available_deals), 2):
        chiefsList.add(KeyboardButton(available_deals[i - 1].last_name+" "+available_deals[i - 1].name+"\n"+str(available_deals[i - 1].income)),
                         KeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income)))
    if len(available_deals) % 2 != 0:
        i = len(available_deals) - 1
        chiefsList.add(KeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income)))
    
    await message.reply(PHRASES["selectChiefStore"][user_language], reply_markup=chiefsList)

