from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message

LOCALIZATIONS = ["ru", "en"]
COMMANDS = {
    "start" : {
        "ru" : "старт",
        "en" : "start",
        "desc_ru" : "Запускает бота или приветсвие",
        "desc_en" : "Starts the bot",
    },
    "profile" : {
        "ru" : "профиль",
        "en" : "profile",
        "desc_ru" : "Выводит информацию о твоём профиле",
        "desc_en" : "Shows your profile information",
    },
    "language" : {
        "ru" : "язык",
        "en" : "language",
        "desc_ru" : "Смена языка",
        "desc_en" : "Language switch",
    },
    "extensions" : {
        "ru" : "расширения",
        "en" : "extensions",
        "desc_ru" : "Даёт список доступных категорий для расширения",
        "desc_en" : "Shows available extensions",
    },
    "employment" : {
        "ru" : "нанять",
        "en" : "employ",
        "desc_ru" : "Показывает трудовую биржу",
        "desc_en" : "Shows labor exchange",
    },
    "chiefs" : {
        "ru" : "повара",
        "en" : "chiefs",
        "desc_ru" : "Показывает список доступных вам поваров",
        "desc_en" : "Shows list of available chiefs",
    },
    "servants" : {
        "ru" : "официанты",
        "en" : "servants",
        "desc_ru" : "Показывает список доступных вам официантов",
        "desc_en" : "Shows list of available servants",
    },
    "kitchen" : {
        "ru" : "кухня",
        "en" : "kitchen",
        "desc_ru" : "Даёт информацию о требованиях для расширеня кухни",
        "desc_en" : "Shows requirements for kitchen extension",
    },
    "lounge" : {
        "ru" : "зал",
        "en" : "lounge",
        "desc_ru" : "Даёт информацию о требованиях для расширеня зала",
        "desc_en" : "Shows requirements for lounge extension",
    },
    "extend_kitchen" : {
        "ru" : "расширить_кухню",
        "en" : "extend_kitchen",
        "desc_ru" : "Покупает расширение кухни",
        "desc_en" : "Buys kitchen extension",
    },
    "extend_lounge" : {
        "ru" : "расширить_зал",
        "en" : "extend_lounge",
        "desc_ru" : "Покупает расширение зала",
        "desc_en" : "Buys lounge extension",
    },
    "start_shift" : {
        "ru" : "открытие",
        "en" : "open",
        "desc_ru" : "начинает рабочую смену",
        "desc_en" : "opens restourant for today",
    },
    "tax_check" : {
        "ru" : "налоговая_проверка",
        "en" : "tax_check",
        "desc_ru" : "Подкупает налоговую службу для проверки",
        "desc_en" : "Bribes the tax service to check",
    },
    "brawl" : {
        "ru" : "дебош",
        "en" : "brawl",
        "desc_ru" : "Подкупает бомжей для дебоша",
        "desc_en" : "Bribes homeless people for debauchery",
    },
    "help" : {
        "ru" : "помощь",
        "en" : "help",
        "desc_ru" : "Выводит инструкции к боту либо к опреденной команде",
        "desc_en" : "Outputs instructions to the bot or to a specific command",
    },
}
PHRASES = {
    "default_help" : {
        "ru" : "Станьте виртуальным владельцем ресторана с помощью \"Ресто-мастер\" - увлекательного телеграм бота! Управляйте меню, обучайте персонал, привлекайте клиентов и развивайте свой ресторан.",
        "en" : "Become a virtual restaurant owner with \"Resto-Master\" - an engaging Telegram bot! Manage menus, train staff, attract customers, and grow your restaurant.",
    },
    "languageChange" : {
        "ru" : "Язык успешно изменён на Русский",
        "en" : "Language changed successfully to English",
    },
    "greeting" : {
        "ru" : "Привет!\nВ этом боте ты можешь создать свой собственный ресторан с нуля, а также соревноваться со своими друзьями",
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
        "ru" : "Хочешь купить?",
        "en" : "Do you agree to buy?",
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
        "ru" : "Не хватает пространтсва. Попробуй расширить заведение",
        "en" : "Not enough space. Try extending building",
    },
    "successful_deal" :{
        "ru" : "Успешная покупка",
        "en" : "Bought successfully",
    },
    "extension_category" :{
        "ru" : "Выбери что хочешь расширить",
        "en" : "Select extension",
    },
    "k_stats" : {
        "ru" : "текущая вместимость кухни - ",
        "en" : "current kitchen workload - ",
    },
    "k_tip" : {
        "ru" : "Используй /"+COMMANDS["extend_kitchen"]["ru"]+" для расширения кухни",
        "en" : "Use /"+COMMANDS["extend_kitchen"]["en"]+" to extend kitchen",
    },
    "l_stats" : {
        "ru" : "текущая вместимость зала - ",
        "en" : "current restourant lounge workload - ",
    },
    "l_tip" : {
        "ru" : "Используй /"+COMMANDS["extend_lounge"]["ru"]+" для расширения зала",
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
        "ru" : "Ты успешно уклонился от налогов",
        "en" : "You skipped taxes",
    },
    "tax_skipped_fail" : {
        "ru" : "Тебя накрыла налоговая проверка. Ты заплатили за все свои уклонения: {fine}$",
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
        "ru" : "Бомжи наняты и уже движутся к ресторану \"{name}\".\nТвоего конкурента ждёт неприятная смена!",
        "en" : "Brawlers are hired and already in \"{name}\".\nIt would be bad day for your opponent!",
    },
    "incorrect_command" : {
        "ru" : "Команда \"{command}\" не найдена",
        "en" : "Command \"{command}\" not found",
    },
    "brawl_self" : {
        "ru" : "Глупо заказывать дебош в свой же ресторан!",
        "en" : "You can't order a brawl in your own restourant!",
    },
    "profile_template" : {
        "ru" : "{fullname}\nID: {user_id}\nЯзык: {language}\nБаланс: {balance}\n\nРесторан \"{restName}\"\nДоход: {restIncome}\nНалоговая задолжность: {restTaxDebt}\nПоследняя смена: {lastActive}\n\nКухня\nКол-во поваров: {kitchenWorkload}\nМакс поваров: {kitchenWorkloadMax}\n\nЗал\nКол-во официантов: {loungeWorkload}\nМакс официантов: {loungeWorkloadMax}",
        "en" : "{fullname}\nID: {user_id}\nLanguage: {language}\nBalance: {balance}\n\nRestourant \"{restName}\"\nIncome: {restIncome}\nTax debt: {restTaxDebt}\nLast active: {lastActive}\n\nKitchen\nChiefs count: {kitchenWorkload}\nMax chiefs: {kitchenWorkloadMax}\n\nLounge\nservants count: {loungeWorkload}\nMax servants: {loungeWorkloadMax}",
    },
}

def get_localization_buttons() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardMarkup()
    for i in range(len(LOCALIZATIONS)):
        buttons.add(InlineKeyboardButton(LOCALIZATIONS[i], callback_data=LOCALIZATIONS[i]))
    return buttons

def check_command_localization(command : str, message : Message, command_only: bool) -> str | None:
    text = ""
    if message.is_command():
        text = message.get_command(True)
    else:
        if command_only:
            return None
        text = message.text
    for key, item in COMMANDS[command].items():
        if item == text:
            return key
    return None

def get_command_description(command : str, user_language: str) -> str | None:
    cKey = None
    for key, item in COMMANDS.items():
        for language, com in item.items():
            if com == command:
                cKey = key
                break
        if cKey is not None:
            break
    if cKey is None:
        return None
    if "desc_"+user_language not in COMMANDS[cKey].keys():
        return None
    return COMMANDS[cKey]["desc_"+user_language]
    