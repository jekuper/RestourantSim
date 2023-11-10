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
    dpG.register_message_handler(process_duel, lambda msg: BotLocalization.check_command_localization("duel", msg, False) is not None, state=[None])
    dpG.register_message_handler(process_coin, lambda msg: BotLocalization.check_command_localization("coin", msg, False) is not None, state=[None])
    dpG.register_message_handler(process_crash, lambda msg: BotLocalization.check_command_localization("crash", msg, False) is not None, state=[None])
    
    dpG.register_callback_query_handler(process_callback_duel, regexp=r"duel_(agree|disagree)_\d+_\d+_\d+", state=[None])

    if common.dp is None:
        common.dp = dpG

async def process_duel(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    cost = 50

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
        await message.reply(PHRASES["duel_self"][user_language])
        return

    if cost <= BotDataBase.get_balance(message.from_id) and cost <= BotDataBase.get_balance(target_id):
        target_language = BotDataBase.get_user_language(target_id)
        buttons = InlineKeyboardMarkup()
        buttons.add(InlineKeyboardButton(PHRASES["agree"][target_language], callback_data="duel_agree_"+str(target_id)+"_"+str(message.from_id)+"_"+str(cost)), 
                    InlineKeyboardButton(PHRASES["disagree"][target_language], callback_data="duel_disagree_"+str(target_id)+"_"+str(message.from_id)+"_"+str(cost)))

        await message.reply((PHRASES["duel_check"][target_language]).format(target=message.reply_to_message.from_id,
                                                                           initiator=message.from_id,
                                                                           targetName=message.reply_to_message.from_user.full_name,
                                                                           initiatorName=message.from_user.full_name,
                                                                           cost = cost), reply_markup=buttons)
    else:
        await message.reply(PHRASES["not_enough_balance"][user_language].format(price=str(cost)))

async def process_coin(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    cost = 50

    if message.is_command() and message.get_args() is not None and message.get_args().isnumeric():
        cost = int(message.get_args())

    if cost <= BotDataBase.get_balance(message.from_id):
        if BotDataBase.bool_based_on_probability(0.3):
            BotDataBase.change_balance(message.from_id, cost)
            await message.reply(PHRASES["coin_win"][user_language].format(cost=cost))
        else:
            BotDataBase.change_balance(message.from_id, -cost)
            await message.reply(PHRASES["coin_lose"][user_language].format(cost=cost))
    else:
        await message.reply(PHRASES["not_enough_balance"][user_language].format(price=str(cost)))

async def process_crash(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    cost = 50
    kf = 1

    if message.is_command() and message.get_args() is not None:
        args = message.get_args().split()
        if len(args) < 2:
            await message.reply(PHRASES["incorrect_command"][user_language].format(command=COMMANDS["crash"]["us"]))
            return
        cost = int(args[0])
        kf = float(args[1])
        if kf < 1 or kf > 10 or cost < 0:
            await message.reply(PHRASES["incorrect_command"][user_language].format(command=COMMANDS["crash"]["us"]))
            return

        if cost <= BotDataBase.get_balance(message.from_id):
            BotDataBase.change_balance(message.from_id, -cost)
            newKf = 1000
            for _ in range(18):
                newKf = min(newKf, BotDataBase.random_float(1, 10))
            if newKf > kf:
                BotDataBase.change_balance(message.from_id, int(cost * kf))
                await message.reply(PHRASES["crash_win"][user_language].format(cost=int(cost * kf), kf=newKf, profit=(int(cost * kf) - cost)))
            else:
                await message.reply(PHRASES["crash_lose"][user_language].format(cost=cost, kf=newKf, profit=(int(cost * kf) - cost)))
        else:
            await message.reply(PHRASES["not_enough_balance"][user_language].format(price=str(cost)))


async def process_callback_duel(callback_query: types.CallbackQuery, state: FSMContext):
    decesion = callback_query.data.split("_")[1]
    target_id = int(callback_query.data.split("_")[2])
    initiator_id = int(callback_query.data.split("_")[3])
    cost = int(callback_query.data.split("_")[4])

    if BotDataBase.get_restourant(target_id) is None or BotDataBase.get_restourant(initiator_id) is None:
        await callback_query.message.edit_text(PHRASES["user_not_exist"][user_language])
        return
    
    if callback_query.from_user.id != target_id:
        await callback_query.answer(PHRASES["you_not_target"][BotDataBase.get_user_language(callback_query.from_user.id)])
        return
    user_language = BotDataBase.get_user_language(target_id)
    
    if decesion == "disagree":
        await callback_query.message.edit_text(PHRASES["duel_disagree"][user_language].format(target=target_id, targetName=callback_query.from_user.full_name))
        return  

    if BotDataBase.get_balance(target_id) >= cost and BotDataBase.get_balance(initiator_id) >= cost:
        targetName = callback_query.from_user.full_name
        initiatorName = callback_query.message.reply_to_message.from_user.full_name
        if BotDataBase.bool_based_on_probability():
            target_id, initiator_id = initiator_id, target_id
            targetName, initiatorName = initiatorName, targetName
        BotDataBase.change_balance(target_id, -cost)  
        BotDataBase.change_balance(initiator_id, cost)  
        await callback_query.message.edit_text(PHRASES["duel_result"][user_language].format(prize=str(cost), target=initiator_id, targetName=initiatorName), reply_markup=None)
    else:
        await callback_query.message.edit_text(PHRASES["not_enough_balance"][user_language].format(price=str(cost)), reply_markup=None)


