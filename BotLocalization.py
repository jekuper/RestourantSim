from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import Message
from aiogram.utils.emoji import emojize

LOCALIZATIONS = ["ru", "us"]
COMMANDS = {
    "start" : {
        "ru" : "старт",
        "us" : "start",
        "desc_ru" : emojize("Запускает бота или приветсвие:waving_hand:"),
        "desc_us" : emojize("Starts the bot:waving_hand:"),
    },
    "profile" : {
        "ru" : "профиль",
        "us" : "profile",
        "desc_ru" : emojize(":bust_in_silhouette: Выводит информацию о твоём профиле"),
        "desc_us" : emojize(":bust_in_silhouette: Shows your profile information"),
    },
    "language" : {
        "ru" : "язык",
        "us" : "language",
        "desc_ru" : emojize(":globe_showing_europe_africa: Смена языка"),
        "desc_us" : emojize(":globe_showing_europe_africa: Language switch"),
    },
    "extensions" : {
        "ru" : "расширения",
        "us" : "extensions",
        "desc_ru" : emojize(":left_right_arrow: Даёт список доступных категорий для расширения"),
        "desc_us" : emojize(":left_right_arrow: Shows available extensions"),
    },
    "employment" : {
        "ru" : "нанять",
        "us" : "employ",
        "desc_ru" : emojize(":identification_card: Показывает трудовую биржу"),
        "desc_us" : emojize(":identification_card: Shows labor exchange"),
    },
    "chiefs" : {
        "ru" : "повара",
        "us" : "chiefs",
        "desc_ru" : emojize(":man_cook: Показывает список доступных вам поваров"),
        "desc_us" : emojize(":man_cook: Shows list of available chiefs"),
    },
    "servants" : {
        "ru" : "официанты",
        "us" : "servants",
        "desc_ru" : emojize(":person_tipping_hand: Показывает список доступных вам официантов"),
        "desc_us" : emojize(":person_tipping_hand: Shows list of available servants"),
    },
    "kitchen" : {
        "ru" : "кухня",
        "us" : "kitchen",
        "desc_ru" : emojize(":kitchen_knife: Даёт информацию о требованиях для расширеня кухни"),
        "desc_us" : emojize(":kitchen_knife: Shows requirements for kitchen extension"),
    },
    "lounge" : {
        "ru" : "зал",
        "us" : "lounge",
        "desc_ru" : emojize(":chair: Даёт информацию о требованиях для расширеня зала"),
        "desc_us" : emojize(":chair: Shows requirements for lounge extension"),
    },
    "extend_kitchen" : {
        "ru" : "расширить_кухню",
        "us" : "extend_kitchen",
        "desc_ru" : emojize(":handshake::kitchen_knife: Покупает расширение кухни"),
        "desc_us" : emojize(":handshake::kitchen_knife: Buys kitchen extension"),
    },
    "extend_lounge" : {
        "ru" : "расширить_зал",
        "us" : "extend_lounge",
        "desc_ru" : emojize(":handshake::chair: Покупает расширение зала"),
        "desc_us" : emojize(":handshake::chair: Buys lounge extension"),
    },
    "start_shift" : {
        "ru" : "открытие",
        "us" : "open",
        "desc_ru" : emojize(":money_bag: начинает рабочую смену"),
        "desc_us" : emojize(":money_bag: opens restourant for today"),
    },
    "tax_check" : {
        "ru" : "налоговая_проверка",
        "us" : "tax_check",
        "desc_ru" : emojize(":man_detective: Подкупает налоговую службу для проверки"),
        "desc_us" : emojize(":man_detective: Bribes the tax service to check"),
    },
    "brawl" : {
        "ru" : "дебош",
        "us" : "brawl",
        "desc_ru" : emojize(":troll: Подкупает бомжей для дебоша"),
        "desc_us" : emojize(":troll: Bribes homeless people for debauchery"),
    },
    "help" : {
        "ru" : "помощь",
        "us" : "help",
        "desc_ru" : emojize(":ambulance: Выводит инструкции к боту либо к опреденной команде"),
        "desc_us" : emojize(":ambulance: Outputs instructions to the bot or to a specific command"),
    },
    "duel" : {
        "ru" : "дуель",
        "us" : "duel",
        "desc_ru" : emojize(":crossed_swords: Вызывает игрока на дуель. Нужно послать ответом на сообщение игрока который является целью"),
        "desc_us" : emojize(":crossed_swords: Challenges the player to a duel. You need to send a response to the message of the player who is the target"),
    },
    "coin" : {
        "ru" : "монетка",
        "us" : "coin",
        "desc_ru" : emojize(":coin: Подбрасывает монетку. Есть шанс удвоить ставку"),
        "desc_us" : emojize(":coin: Flips a coin. There is a chance to double the bet"),
    },
    "crash" : {
        "ru" : "краш",
        "us" : "crash",
        "desc_ru" : emojize(":chart_increasing: Начинает игру в краш. \n2 обязательных аргумента: ставка и коеффициент"),
        "desc_us" : emojize(":chart_increasing: Starts crash game\n 2 required arguments: bet amount and coefficient"),
    },
    "transfer" : {
        "ru" : "перевод",
        "us" : "transfer",
        "desc_ru" : emojize("переводи деньги. \n2 обязательных аргумента: получатель и сумма"),
        "desc_us" : emojize("transfers money. \n2 required arguments: receiver and amount"),
    },
    "name" : {
        "ru" : "имя",
        "us" : "name",
        "desc_ru" : emojize("Смена имени ресторана"),
        "desc_us" : emojize("Changes restourant's name"),
    },
}
PHRASES = {
    "default_help": {
        "ru": "🍽️ Станьте виртуальным владельцем ресторана с помощью \"Ресто-мастер\" - увлекательного телеграм бота! Управляйте меню, обучайте персонал, привлекайте клиентов и развивайте свой ресторан.",
        "us": "🍽️ Become a virtual restaurant owner with \"Resto-Master\" - an engaging Telegram bot! Manage menus, train staff, attract customers, and grow your restaurant."
    },
    "languageChange": {
        "ru": "🌐 Язык успешно изменён на Русский",
        "us": "🌐 Language changed successfully to English"
    },
    "greeting": {
        "ru": "👋 Привет!\nВ этом боте ты можешь создать свой собственный ресторан с нуля, а также соревноваться со своими друзьями",
        "us": "👋 Hi! In this bot you can create your own restaurant"
    },
    "selectName": {
        "ru": "💡 Выбери имя для своего ресторана!",
        "us": "💡 Type a name for your restaurant!"
    },
    "invalidName": {
        "ru": "🚫 Имя должно включать в себя только латинские буквы или кириллицу, цифры, пробел и _",
        "us": "🚫 Name must include only Latin characters, cyrillic, numbers, space, _"
    },
    "nameSet": {
        "ru": "✅ Имя успешно установлено\nТеперь тебе нужно нанять свой первый персонал!\n\nОткрыть рынок рабочих - /" + COMMANDS["employment"]["ru"],
        "us": "✅ Name set successfully/\nNow you need to hire new employees!\n\nOpen store - /" + COMMANDS["employment"]["us"]
    },
    "storeCategory": {
        "ru": "🛒 Выбери категорию покупки",
        "us": "🛒 Select shop category"
    },
    "selectChiefStore": {
        "ru": "👩‍🍳 Выбери повара, которого хотите нанять",
        "us": "👩‍🍳 Select a chef to hire"
    },
    "selectServantStore": {
        "ru": "👩‍🍳 Выбери официанта, которого хотите нанять",
        "us": "👩‍🍳 Select a servant to hire"
    },
    "human_deal_not_found": {
        "ru": "❌ Такая сделка больше не существует",
        "us": "❌ Selected deal no longer exists"
    },
    "deal_confirmation": {
        "ru": "🤝 Хочешь купить?",
        "us": "🤝 Do you agree to buy?"
    },
    "agree": {
        "ru": "✅ Согласен",
        "us": "✅ Agree"
    },
    "disagree": {
        "ru": "❌ Не согласен",
        "us": "❌ Disagree"
    },
    "income": {
        "ru": "💰 прибыль",
        "us": "💰 income"
    },
    "cost": {
        "ru": "💲 цена",
        "us": "💲 cost"
    },
    "job_type": {
        "ru": "👨‍🍳 Должность",
        "us": "👨‍🍳 Job"
    },
    "not_enough_balance": {
        "ru": "❌ Не хватает денег.\n💲 Цена: {price}$",
        "us": "❌ Not enough balance.\n💲 Cost: {price}$"
    },
    "not_enough_income": {
        "ru": "❌ Предложение отклонено человеком\n💲 Требуется доход заведения как минимум: {price}$",
        "us": "❌ Offer declined.\n💲 Minimum income required: {price}$"
    },
    "not_enough_space": {
        "ru": "❌ Не хватает места. Попробуй расширить заведение",
        "us": "❌ Not enough space. Try extending the building"
    },
    "successful_deal": {
        "ru": "✅ Успешная покупка",
        "us": "✅ Bought successfully"
    },
    "extension_category": {
        "ru": "🔍 Выбери, что хочешь расширить",
        "us": "🔍 Select extension"
    },
    "k_stats": {
        "ru": "🍳 Текущая вместимость кухни - ",
        "us": "🍳 Current kitchen workload - "
    },
    "k_tip": {
        "ru": "Используй /"+COMMANDS["extend_kitchen"]["ru"]+" для расширения кухни",
        "us": "Use /"+COMMANDS["extend_kitchen"]["us"]+" to extend the kitchen"
    },
    "l_stats": {
        "ru": "🍽️ Текущая вместимость зала - ",
        "us": "🍽️ Current restaurant lounge workload - "
    },
    "l_tip": {
        "ru": "Используй /"+COMMANDS["extend_lounge"]["ru"]+" для расширения зала",
        "us": "Use /"+COMMANDS["extend_lounge"]["us"]+" to extend the lounge"
    },
    "ext_cost": {
        "ru": "💲 Цена расширения",
        "us": "💲 Extension cost"
    },
    "shift_processed": {
        "ru": "✅ Смена отработала успешно!\n\n💰 Заработано: {income}\n💥 Расходы из-за дебоша: {damage}\n\n💵 Чистая прибыль: {profit}",
        "us": "✅ Day ended!\n\n💰 Income: {income}\n💥 Brawl damage: {damage}\n\n💵 Net profit: {profit}"
    },
    "cant_start_shift": {
        "ru": "⏰ Персоналу требуется отдых!\nНачать работу можно через {hours}ч. {minutes}мин.",
        "us": "⏰ Staff needs rest!\nThe next shift is in {hours}h. {minutes}min."
    },
    "tax_paying": {
        "ru": "💸 Хотите оплатить налоги?\nСумма: {tax}",
        "us": "💸 Want to pay taxes?\nAmount: {tax}"
    },
    "tax_paid": {
        "ru": "✅ Налоги оплачены в размере {tax}$!",
        "us": "✅ Taxes are paid. \nAmount: {tax}"
    },
    "tax_skipped_suc": {
        "ru": "🙅‍♂️ Ты успешно уклонился от налогов",
        "us": "🙅‍♂️ You skipped taxes"
    },
    "tax_skipped_fail": {
        "ru": "🚔 Тебя накрыла налоговая проверка. Ты заплатил за все свои уклонения: {fine}$",
        "us": "🚔 You got caught in a tax check. You paid for all your evasions: {fine}$"
    },
    "tax_check_sent": {
        "ru": "📋 Проверка подкуплена и уже направляется к ресторану \"{name}\". За проверку заплачено: {cost}$",
        "us": "📋 Tax check has been sent to restaurant \"{name}\". You paid: {cost}$"
    },
    "user_not_exist": {
        "ru": "❌ Такого пользователя не существует",
        "us": "❌ User doesn't exist"
    },
    "you_not_target": {
        "ru": "🎯 Ты не цель. Только цель может взаимодействовать с этим сообщением!",
        "us": "🎯 You are not the target. Only the target can interact with this message!"
    },
    "provide_reply": {
        "ru": "📨 Чтобы использовать эту команду, надо отправить её ответом на чьё-либо сообщение",
        "us": "📨 Use this command as a reply to somebody's message"
    },
    "brawl_level_increased": {
        "ru": "👊 Бомжи наняты и уже движутся к ресторану \"{name}\".\nТвоего конкурента ждёт неприятная смена!\nУбытков будет примерно на {cost}$",
        "us": "👊 Brawlers are hired and already in \"{name}\".\nIt will be a bad day for your opponent!\nLosses will be approximately at {cost}$"
    },
    "incorrect_command": {
        "ru": "❓ Команда \"{command}\" введена неверно",
        "us": "❓ Command \"{command}\", not enough arguments provided"
    },
    "brawl_self": {
        "ru": "🤦‍♂️ Глупо заказывать драку в своем же ресторане!",
        "us": "🤦‍♂️ You can't order a brawl in your own restaurant!"
    },
    "duel_self": {
        "ru": "🤦‍♂️ Нельзя бросать дуэль самому себе!",
        "us": "🤦‍♂️ You can't duel yourself!"
    },
    "duel_check": {
        "ru": "🤺 <a href=\"tg://user?id={target}\">{targetName}</a>, принимаете ли вы вызов от <a href=\"tg://user?id={initiator}\">{initiatorName}</a> на сумму {cost}$?",
        "us": "🤺 <a href=\"tg://user?id={target}\">{targetName}</a>, do you accept a duel challenge from <a href=\"tg://user?id={initiator}\">{initiatorName}</a> for {cost}$?"
    },
    "duel_disagree": {
        "ru": "🤷‍♂️ <a href=\"tg://user?id={target}\">{targetName}</a>, отказался!",
        "us": "🤷‍♂️ <a href=\"tg://user?id={target}\">{targetName}</a>, disagreed!"
    },
    "duel_result": {
        "ru": "🎉 <a href=\"tg://user?id={target}\">{targetName}</a>, победил! Выигрыш: {prize}",
        "us": "🎉 <a href=\"tg://user?id={target}\">{targetName}</a>, won! Prize: {prize}"
    },
    "coin_win": {
        "ru": "🤑 Вы победили!\nВы получили {cost}$",
        "us": "🤑 You won!\nYou got {cost}$"
    },
    "coin_lose": {
        "ru": "😞 Вы проиграли\nВы потеряли {cost}$",
        "us": "😞 You lost\nYou lost {cost}$"
    },
    "crash_win": {
        "ru": "🤑 Вы победили, коэффициент: {kf:.2f}\nВы получили {cost}$",
        "us": "🤑 You won, coefficient: {kf:.2f}\nYou got {cost}$"
    },
    "crash_lose": {
        "ru": "💥 Вы проиграли, коэффициент: {kf:.2f}\nВы потеряли {cost}$",
        "us": "💥 You lost, coefficient: {kf:.2f}\nYou lost {cost}$"
    },
    "profile_template": {
        "ru": "👤{fullname}\n🆔ID: <code>{user_id}</code>\n🌐 Язык: {language}\n💰 Баланс: {balance}\n\n🍽️ Ресторан \"{restName}\"\n💰 Доход: {restIncome}\n📋 Налоговая задолженность: {restTaxDebt}\n🕒 Последняя смена: {lastActive}\n\n👨‍🍳 Кухня\n👨‍🍳 Количество поваров: {kitchenWorkload}\n👨‍🍳 Максимальное количество поваров: {kitchenWorkloadMax}\n\n🍽️ Зал\n👩‍🍳 Количество официантов: {loungeWorkload}\n👩‍🍳 Максимальное количество официантов: {loungeWorkloadMax}",
        "us": "👤{fullname}\n🆔ID: <code>{user_id}</code>\n🌐 Language: {language}\n💰 Balance: {balance}\n\n🍽️ Restaurant \"{restName}\"\n💰 Income: {restIncome}\n📋 Tax debt: {restTaxDebt}\n🕒 Last active: {lastActive}\n\n👨‍🍳 Kitchen\n👨‍🍳 Chiefs count: {kitchenWorkload}\n👨‍🍳 Max chiefs: {kitchenWorkloadMax}\n\n🍽️ Lounge\n👩‍🍳 Servants count: {loungeWorkload}\n👩‍🍳 Max servants: {loungeWorkloadMax}"
    },
    "reply_keyboard_removed": {
        "ru": "👌 Понял + принял",
        "us": "👌 Got you"
    },
    "transfer_success": {
        "ru": "💥 Перевод успешен: \nПолучатель: {target}\nСумма: {amount}$",
        "us": "💥 Transfer success: \nReceiver: {target}\nAmount {amount}$"
    },
    "transfer_received": {
        "ru": "🤑 Получен перевод от <code>{sender}</code>: {amount}$",
        "us": "🤑 Transfer received from <code>{sender}</code>: {amount}$"
    },
}

def get_localization_buttons() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardMarkup()
    for i in range(len(LOCALIZATIONS)):
        buttons.add(InlineKeyboardButton(LOCALIZATIONS[i], callback_data=LOCALIZATIONS[i]))
    return buttons

def check_command_localization(command : str, message : Message, command_only: bool) -> str:
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

def get_command_description(command : str, user_language: str) -> str:
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
    