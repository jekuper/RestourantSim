from aiogram.dispatcher import Dispatcher
from aiogram import types
import BotLocalization
import BotDataBase
from aiogram.dispatcher import FSMContext
import handlers.common as common
import json
from BotLocalization import PHRASES, COMMANDS
from datetime import datetime

def register_handlers(dpG: Dispatcher):
    dpG.register_message_handler(process_profile, lambda msg: BotLocalization.check_command_localization("profile", msg, False) is not None, state=None)
    dpG.register_message_handler(process_transfer, lambda msg: BotLocalization.check_command_localization("transfer", msg, True) is not None, state=None)

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

async def process_transfer(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    target = -1
    amount = 0

    if message.is_command() and message.get_args() is not None:
        args = message.get_args().split()
        if len(args) < 2:
            await message.reply(PHRASES["incorrect_command"][user_language].format(command=COMMANDS["transfer"]["us"]))
            return
        target = int(args[0])
        amount = int(args[1])
        if BotDataBase.get_restourant(target) is None:
            await message.reply(PHRASES["user_not_exist"][user_language])
            return
        
        if amount <= BotDataBase.get_balance(message.from_id):
            BotDataBase.change_balance(message.from_id, -amount)
            BotDataBase.change_balance(target, amount)
            await message.reply(PHRASES["transfer_success"][user_language].format(amount=amount, target=target))
            await message.bot.send_message(target, PHRASES["transfer_received"][BotDataBase.get_user_language(target)].format(sender=message.from_id, amount=amount))
        else:
            await message.reply(PHRASES["not_enough_balance"][user_language].format(price=str(amount)))
