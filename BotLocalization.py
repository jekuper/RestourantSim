from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message

LOCALIZATIONS = ["ru", "en"]
COMMANDS = {
    "start" : {
        "ru" : "старт",
        "en" : "start",
    },
    "profile" : {
        "ru" : "профиль",
        "en" : "profile",
    },
    "language" : {
        "ru" : "язык",
        "en" : "language",
    },
    "extensions" : {
        "ru" : "расширения",
        "en" : "extensions",
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
    "kitchen" : {
        "ru" : "кухня",
        "en" : "kitchen",
    },
    "lounge" : {
        "ru" : "зал",
        "en" : "lounge",
    },
    "extend_kitchen" : {
        "ru" : "расширить_кухню",
        "en" : "extend_kitchen",
    },
    "extend_lounge" : {
        "ru" : "расширить_зал",
        "en" : "extend_lounge",
    },
    "start_shift" : {
        "ru" : "открытие",
        "en" : "open",
    },
    "tax_check" : {
        "ru" : "налоговая_проверка",
        "en" : "tax_check",
    },
    "brawl" : {
        "ru" : "дебош",
        "en" : "brawl",
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
    "human_deal_not_found" :{
        "ru" : "Такая сделка больше не существует",
        "en" : "Selected deal no longer exists",
    },
    "deal_confirmation" :{
        "ru" : "Хотите купить?",
        "en" : "Agree to buy?",
    },
    "agree" :{
        "ru" : "Согласен",
        "en" : "Agree",
    },
    "disagree" :{
        "ru" : "Не согласен",
        "en" : "Disagree",
    },
    "income" :{
        "ru" : "прибыль",
        "en" : "income",
    },
    "cost" :{
        "ru" : "цена",
        "en" : "cost",
    },
    "job_type" :{
        "ru" : "Должность",
        "en" : "Job",
    },
    "not_enough_balance" :{
        "ru" : "Не хватает денег.\nЦена: {price}$",
        "en" : "Not enough balance.\nCost: {price}$",
    },
    "not_enough_space" :{
        "ru" : "Не хватает пространтсва. Попробуйте расширить заведение",
        "en" : "Not enough space. Try extending building",
    },
    "successful_deal" :{
        "ru" : "Успешная покупка",
        "en" : "Bought successfully",
    },
    "extension_category" :{
        "ru" : "Выбери что хотим расширить",
        "en" : "Select extension",
    },
    "k_stats" : {
        "ru" : "текущая вместимость кухни - ",
        "en" : "current kitchen workload - ",
    },
    "k_tip" : {
        "ru" : "Используйте /"+COMMANDS["extend_kitchen"]["ru"]+" для расширения кухни",
        "en" : "Use /"+COMMANDS["extend_kitchen"]["en"]+" to extend kitchen",
    },
    "l_stats" : {
        "ru" : "текущая вместимость зала - ",
        "en" : "current restourant lounge workload - ",
    },
    "l_tip" : {
        "ru" : "Используйте /"+COMMANDS["extend_kitchen"]["ru"]+" для расширения кухни",
        "en" : "Use /"+COMMANDS["extend_lounge"]["en"]+" to extend lounge",
    },
    "ext_cost" : {
        "ru" : "Цена расширения",
        "en" : "Extension cost",
    },
    "shift_processed" : {
        "ru" : "Смена отработа успешно!\n\n--------\nЗаработано: {income}\nРасходы из-за дебоша: {damage}\n\nЧистая прибыль: {profit}",
        "en" : "Day ended!\n\n--------\nIncome: {income}\nBrawl damage: {damage}\n\nNet profit: {profit}",
    },
    "cant_start_shift" : {
        "ru" : "Персоналу требуется отдых!\nНачать работу можно через {hours}ч. {minutes}мин.",
        "en" : "Staff need rest!\nThe next shift is in {hours}h. {minutes}min.",
    },
    "tax_paying" : {
        "ru" : "Хотите оплатить налоги?\nСумма: {tax}",
        "en" : "Staff need rest!\nThe next shift is in {hours}h. {minutes}min.",
    },
    "tax_paid" : {
        "ru" : "Налоги оплачены в размере {tax}$!",
        "en" : "Taxes are paid. \nAmount: {tax}",
    },
    "tax_skipped_suc" : {
        "ru" : "Вы успешно уклонились от налогов",
        "en" : "You skipped taxes",
    },
    "tax_skipped_fail" : {
        "ru" : "Вас накрыла налоговая проверка. Вы заплатили за все свои уклонения: {fine}$",
        "en" : "You got caught on a tax check. You paid for all schemas: {fine}$",
    },
    "tax_check_sent" : {
        "ru" : "Проверка подкуплена и уже направляется к ресторану \"{name}\"",
        "en" : "Tax check has been sent to restourant \"{name}\"",
    },
    "user_not_exist" : {
        "ru" : "Такого пользователя не существует",
        "en" : "User doesn't exist",
    },
    "provide_reply" : {
        "ru" : "Чтобы использовать эту команду, надо отправить её ответом на чьё-либо сообщение",
        "en" : "Use this command as a reply to somebodies message",
    },
    "brawl_level_increased" : {
        "ru" : "Бомжи наняты и уже движутся к ресторану \"{name}\".\nВашего конкурента ждёт неприятная смена!",
        "en" : "Brawlers are hired and already in \"{name}\".\nIt would be bad day for your opponent!",
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

    
