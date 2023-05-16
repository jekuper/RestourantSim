from aiogram.dispatcher import Dispatcher
from aiogram import types
import BotLocalization
from BotConfigs import BotStates
import BotDataBase
from aiogram.dispatcher import FSMContext
import handlers.common as common

def register_handlers_greeting(dpG: Dispatcher):
    dpG.register_message_handler(process_start, lambda msg: BotLocalization.check_command_localization("start", msg) is not None, state=None)
    dpG.register_message_handler(process_language_switch, lambda msg: BotLocalization.check_command_localization("language", msg) is not None, state=None)
    dpG.register_message_handler(process_restaurant_name, state=BotStates.SELECTING_NAME)

    dpG.register_callback_query_handler(process_callback_localization, text=BotLocalization.LOCALIZATIONS, state=[BotStates.LANGUAGE_SWITCH, BotStates.FIRST_LANGUAGE_SWITCH])

    common.dp = dpG

async def process_start(message: types.Message, state: FSMContext):
        
    if BotDataBase.insert_new_user(message.from_id):
        await message.reply("Выбери язык удобный для тебя\n\nPlease select language", reply_markup=BotLocalization.get_localization_buttons())
        await BotStates.FIRST_LANGUAGE_SWITCH.set()
    else:
        await message.reply(BotLocalization.PHRASES["greeting"][BotDataBase.get_user_language(message.from_id)])

async def process_language_switch(message: types.Message, state: FSMContext):
    await message.reply("Выбери язык удобный для тебя\n\nPlease select language", reply_markup=BotLocalization.get_localization_buttons())
    await BotStates.LANGUAGE_SWITCH.set()

async def process_callback_localization(callback_query: types.CallbackQuery, state: FSMContext):
    BotDataBase.update_user_settings(callback_query.from_user.id, callback_query.data)
    await callback_query.answer(BotLocalization.PHRASES["languageChange"][callback_query.data])
    await callback_query.message.edit_text(BotLocalization.PHRASES["languageChange"][callback_query.data])

    current_state = await state.get_state()
    if current_state == BotStates.FIRST_LANGUAGE_SWITCH.state:
        await callback_query.message.reply(BotLocalization.PHRASES["selectName"][BotDataBase.get_user_language(callback_query.from_user.id)])
        await BotStates.SELECTING_NAME.set()
    else:
        await state.finish()

async def process_restaurant_name(message: types.Message, state: FSMContext):
    if not message.text.isalnum():
        await message.reply(BotLocalization.PHRASES["invalidName"][BotDataBase.get_user_language(message.from_id)])
        return
    
    BotDataBase.set_restourant_name(message.from_id, message.text)
    await message.reply(BotLocalization.PHRASES["nameSet"][BotDataBase.get_user_language(message.from_id)])
    await state.set_state(BotStates.FIRST_WORKER)
    await state.finish()