from aiogram.dispatcher import Dispatcher
from aiogram import types
import BotLocalization
import BotDataBase
from aiogram.dispatcher import FSMContext
import handlers.common as common
import json
from BotLocalization import PHRASES
from datetime import datetime

def register_handlers(dpG: Dispatcher):
    dpG.register_message_handler(process_profile, lambda msg: BotLocalization.check_command_localization("profile", msg, False) is not None, state=None)

    if common.dp is None:
        common.dp = dpG

async def process_profile(message: types.Message, state: FSMContext):
    result = ""
    property = BotDataBase.get_property(message.from_id)
    settings = BotDataBase.get_user_settings(message.from_id)
    rest = BotDataBase.get_restourant(message.from_id)
    user_language = BotDataBase.get_user_language(message.from_id)
    
    result = PHRASES["profile_template"][user_language].format(fullname=message.from_user.full_name, 
                                                language=settings.language, 
                                                user_id=str(settings.user_id), 
                                                balance=str(property.balance),
                                                restName=rest.name,
                                                restTaxDebt=str(rest.tax_debt),
                                                restIncome=str(rest.income),
                                                kitchenWorkload=str(rest.kitchen_workload),
                                                kitchenWorkloadMax=str(rest.kitchen_workload_max),
                                                loungeWorkload=str(rest.lounge_workload),
                                                loungeWorkloadMax=str(rest.lounge_workload_max),
                                                lastActive=rest.last_active.strftime("%m/%d/%Y, %H:%M:%S"),
                                                )
    await message.reply(result)