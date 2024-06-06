from typing import List

from telebot.types import Message

from loader import bot

from database.models import User, History


@bot.message_handler(commands=["history"])
def handle_history(message: Message) -> None:
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    history: List[History] = user.history.order_by(
        -History.time_req, -History.id_req
    ).limit(10)

    result = []
    result.extend(map(str, history))
    if not result:
        bot.send_message(message.from_user.id, "У вас ещё нет запросов")
        return
    bot.send_message(message.from_user.id, "\n".join(result))
