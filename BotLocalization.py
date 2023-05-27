from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message

LOCALIZATIONS = ["ru", "en"]
COMMANDS = {
    "start" : {
        "ru" : "старт",
        "en" : "start",
    },
    "language" : {
        "ru" : "язык",
        "en" : "language",
    },
    "employment" : {
        "ru" : "нанять",
        "en" : "employ",
    },
    "chiefs" : {
        "ru" : "повара",
        "en" : "chiefs",
    },
    "servants" : {
        "ru" : "официанты",
        "en" : "servants",
    },
}
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
        "ru" : "Имя успешно установлено\nТеперь тебе нужно нанять свой первый персонал!\n\nОткрыть рынок рабочих - /"+COMMANDS["employment"]["ru"],
        "en" : "Name set successfully/\nNow you need to hire new employees!\n\nOpen store - /"+COMMANDS["employment"]["en"],
    },
    "storeCategory" :{
        "ru" : "Выбери категорию покупки",
        "en" : "Select shop category",
    },
    "selectChiefStore" :{
        "ru" : "Выбери повара которого хотите нанять",
        "en" : "Select chief to hire",
    },
    "selectServantStore" :{
        "ru" : "Выбери официанта которого хотите нанять",
        "en" : "Select servant to hire",
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

    
