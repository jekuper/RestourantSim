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
    dpG.register_message_handler(process_help, lambda msg: BotLocalization.check_command_localization("help", msg, True) is not None, state=[None])
    
    if common.dp is None:
        common.dp = dpG

async def process_help(message: types.Message, state: FSMContext):
    user_language = BotDataBase.get_user_language(message.from_id)
    
    args = message.get_args()

    if args is not None and args != "":
        if not args.isalpha():
            await message.reply(PHRASES["incorrect_command"][user_language].format(command=args))
            return
        description = BotLocalization.get_command_description(args, user_language)
        if description is None:
            await message.reply(PHRASES["incorrect_command"][user_language].format(command=args))
        else:
            await message.reply(description)
    else:
        await message.reply(PHRASES["default_help"][user_language])
