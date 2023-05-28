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
    dpG.register_message_handler(process_category, lambda msg: BotLocalization.check_command_localization("employment", msg) is not None, state=[BotStates.FIRST_WORKER, None])
    dpG.register_message_handler(process_chiefs_store, lambda msg: BotLocalization.check_command_localization("chiefs", msg) is not None, state=[None])
    dpG.register_message_handler(process_servant_store, lambda msg: BotLocalization.check_command_localization("servants", msg) is not None, state=[None])

    dpG.register_callback_query_handler(process_callback_human_select, regexp=r"human_\d+", state=[None])
    dpG.register_callback_query_handler(process_callback_deal_completion, state=[BotStates.COMPLETING_DEAL])

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
    servantsList = InlineKeyboardMarkup()
    prefix = "human_"
    user_language = BotDataBase.get_user_language(message.from_id)
    
    available_deals = BotDataBase.get_available_human_deals(message.from_id, BotDataBase.job_types.servant)

    for i in range(1, len(available_deals), 2):
        servantsList.add(InlineKeyboardButton(available_deals[i - 1].last_name+" "+available_deals[i - 1].name+"\n"+str(available_deals[i - 1].income), callback_data=prefix+str(available_deals[i - 1].id)),
                         InlineKeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income), callback_data=prefix+str(available_deals[i].id)))
    if len(available_deals) % 2 != 0:
        i = len(available_deals) - 1
        servantsList.add(InlineKeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income), callback_data=prefix+str(available_deals[i].id)))
    
    await message.reply(PHRASES["selectServantStore"][user_language], reply_markup=servantsList)

async def process_chiefs_store(message: types.Message, state: FSMContext):
    chiefsList = InlineKeyboardMarkup()
    prefix = "human_"
    user_language = BotDataBase.get_user_language(message.from_id)
    
    available_deals = BotDataBase.get_available_human_deals(message.from_id, BotDataBase.job_types.chief)

    for i in range(1, len(available_deals), 2):
        chiefsList.add(InlineKeyboardButton(available_deals[i - 1].last_name+" "+available_deals[i - 1].name+"\n"+str(available_deals[i - 1].income), callback_data=prefix+str(available_deals[i - 1].id)),
                         InlineKeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income), callback_data=prefix+str(available_deals[i].id)))
    if len(available_deals) % 2 != 0:
        i = len(available_deals) - 1
        chiefsList.add(InlineKeyboardButton(available_deals[i].last_name+" "+available_deals[i].name+"\n"+str(available_deals[i].income), callback_data=prefix+str(available_deals[i].id)))
    
    await message.reply(PHRASES["selectChiefStore"][user_language], reply_markup=chiefsList)

def get_human_deal_message(deal: BotDataBase.human_deal, language: str):
    result = ""
    result += deal.last_name + " " + deal.name + "\n"
    result += PHRASES["job_type"][language] + ": " +deal.job_type.name + "\n"
    result += PHRASES["income"][language] + ": " + str(deal.income) + "$\n"
    result += "-------\n\n"
    result += PHRASES["cost"][language] + ": " + str(deal.cost) + "$"
    return result

async def process_callback_human_select(callback_query: types.CallbackQuery, state: FSMContext):
    user_language = BotDataBase.get_user_language(callback_query.from_user.id)
    deal = BotDataBase.get_human_deal(int(callback_query.data.replace("human_", "")))
    if deal is None:
        await callback_query.message.edit_text(PHRASES["human_deal_not_found"][user_language])
        return
    
    markup = InlineKeyboardMarkup()
    if BotDataBase.get_balance(callback_query.from_user.id) >= deal.cost:
        markup.add(InlineKeyboardButton(PHRASES["agree"][user_language], callback_data="agree"), InlineKeyboardButton(PHRASES["disagree"][user_language], callback_data="disagree"))
        await BotStates.COMPLETING_DEAL.set()
        await state.update_data(selected_deal=deal)
        await callback_query.message.edit_text(PHRASES["deal_confirmation"][user_language]+"\n\n"+get_human_deal_message(deal, user_language), reply_markup=markup)
    else:
        await callback_query.message.edit_text(PHRASES["not_enough_balance"][user_language]+":\n\n"+get_human_deal_message(deal, user_language), reply_markup=None)
    
async def process_callback_deal_completion(callback_query: types.CallbackQuery, state: FSMContext):
    user_language = BotDataBase.get_user_language(callback_query.from_user.id)
    
    state_data = await state.get_data()
    deal: BotDataBase.human_deal = state_data["selected_deal"]

    if callback_query.data == "disagree":
        await callback_query.message.delete()
        await state.finish()
        return

    if BotDataBase.get_balance(callback_query.from_user.id) >= deal.cost:
        BotDataBase.buy_human(callback_query.from_user.id, deal)
        await callback_query.message.edit_text(PHRASES["successful_deal"][user_language]+"!\n\n", reply_markup=None)
    else:
        await callback_query.message.edit_text(PHRASES["not_enough_balance"][user_language]+":\n\n"+get_human_deal_message(deal, user_language), reply_markup=None)
    await state.finish()
