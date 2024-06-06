from telebot.types import Message

from loader import bot

from database.models import User

from States.states import UserState


@bot.message_handler(commands=["custom"])
def handle_get_custom(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    bot.send_message(user_id, "Вывести коэффициент в диапазоне от и до")
    bot.send_message(user_id, "Введите ОТ какого числа и ДО какого числа, через ПРОБЕЛ")
    bot.set_state(message.from_user.id, UserState.custom_val)
