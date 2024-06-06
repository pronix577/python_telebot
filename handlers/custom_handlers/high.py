from telebot.types import Message

from loader import bot

from database.models import User, Games

from utils.misc.log_request import log_request


@bot.message_handler(commands=["high"])
def handle_high_val(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    bot.send_message(user_id, "Вывожу максимальный коэффициент")
    min_price = Games.select().order_by(Games.price.desc()).limit(1).get()
    record_with_min_price = Games.select().where(Games.price == min_price.price).get()
    result = (
        f"Домашняя команда - {record_with_min_price.home_team}\n"
        f"Гостевая команда - {record_with_min_price.away_team}\n"
        f"Букмекер - {record_with_min_price.title}\n"
        f"Максимальный коэффициент на {record_with_min_price.name_team} - {record_with_min_price.price}"
    )
    bot.send_message(user_id, result)
    log_request(message.from_user.id, message.from_user.first_name, "/high", result)
