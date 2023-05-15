from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message

LOCALIZATIONS = ["ru", "en"]
PHRASES = {
    "languageChange" : {
        "ru" : "Язык успешно изменён на Русский",
        "en" : "Language changed successfully to English",
    },
    "greeting" : {
        "ru" : "Привет!\nВ этом боте ты можешь создать свой собственный ресторан с нуля, а также соревновать со своими друзьями",
        "en" : "Hi! In this bot you can create your own restourant",
    },
    "selectName" :{
        "ru" : "Выбери имя для своего ресторана!",
        "en" : "Type name for your restaurant!",
    },
    "invalidName" :{
        "ru" : "Имя должно включать себя только латинские буквы и цифры",
        "en" : "Name must include only latin characters and numbers",
    },
    "nameSet" :{
        "ru" : "Имя успешно установлено",
        "en" : "Name set successfully",
    },
}
COMMANDS = {
    "start" : {
        "ru" : "старт",
        "en" : "start",
    },
    "language" : {
        "ru" : "язык",
        "en" : "language",
    },
}

def get_localization_buttons() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardMarkup()
    for i in range(len(LOCALIZATIONS)):
        buttons.add(InlineKeyboardButton(LOCALIZATIONS[i], callback_data=LOCALIZATIONS[i]))
    return buttons

def check_command_localization(command : str, message : Message) -> bool:
    text = ""
    if message.is_command():
        text = message.get_command(True)
    else:
        text = message.text
    for key, item in COMMANDS[command].items():
        if item == text:
            return key
    return None

    
