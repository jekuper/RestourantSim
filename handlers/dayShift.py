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
    dpG.register_message_handler(process_shift, lambda msg: BotLocalization.check_command_localization("start_shift", msg) is not None, state=[None])
    dpG.register_callback_query_handler(process_callback_tax_responce, regexp=r"tax_(agree|disagree)_\d+", state=[None])
    
    if common.dp is None:
        common.dp = dpG

async def process_shift(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)

    if BotDataBase.can_start_shift(message.from_id):
        income = BotDataBase.get_income(message.from_id)
        damage = BotDataBase.get_brawl_damage(message.from_id)
        BotDataBase.nullify_brawl_damage(message.from_id)
        tax = int(income // 2)
        BotDataBase.change_balance(message.from_id, income - damage)
        BotDataBase.record_active(message.from_id)
        await message.reply(PHRASES["shift_processed"][user_language].format(income=str(income), damage=str(damage), profit=str(income-damage)))

        
        choice = InlineKeyboardMarkup()
        choice.add(InlineKeyboardButton(PHRASES["agree"][user_language], callback_data="tax_agree_"+str(tax)), 
                   InlineKeyboardButton(PHRASES["disagree"][user_language], callback_data="tax_disagree_"+str(tax)))
        await message.reply(PHRASES["tax_paying"][user_language].format(tax=str(tax)), reply_markup=choice)
    else:
        wait_time = BotDataBase.get_wait_time(message.from_id)
        hours = int(wait_time.total_seconds() // 3600)
        minutes = int((wait_time.total_seconds() - (hours * 3600)) // 60)
        await message.reply(PHRASES["cant_start_shift"][user_language].format(hours=hours, minutes=minutes))

async def process_callback_tax_responce(callback_query: types.CallbackQuery, state: FSMContext):
    user_language = BotDataBase.get_user_language(callback_query.from_user.id)
    responce = True
    tax = int(callback_query.data.split("_")[2])

    if "tax_disagree" in callback_query.data:
        responce = False
    if responce:
        BotDataBase.change_balance(callback_query.from_user.id, -tax)
        await callback_query.message.edit_text(PHRASES["tax_paid"][user_language].format(tax=str(tax)), reply_markup=None)
    else:
        BotDataBase.change_debt(callback_query.from_user.id, tax)
        total_tax = BotDataBase.get_total_debt(callback_query.from_user.id)
        if BotDataBase.bool_based_on_probability(0.9):
            await callback_query.message.edit_text(PHRASES["tax_skipped_suc"][user_language], reply_markup=None)
        else:
            BotDataBase.nullify_debt(callback_query.from_user.id)
            BotDataBase.change_balance(callback_query.from_user.id, -total_tax)
            
            await callback_query.message.edit_text(PHRASES["tax_skipped_fail"][user_language].format(fine=str(total_tax)), reply_markup=None)