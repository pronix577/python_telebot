from telebot.types import Message

from loader import bot

from peewee import IntegrityError

from database.models import User
from utils.misc.check_data import check_request_data


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, "Добро пожаловать в букмекер!")
    except IntegrityError:
        bot.reply_to(message, f"Рад вас снова видеть, {message.from_user.full_name}!")
    check_request_data()


@bot.message_handler(content_types="text")
def message_reply(message: Message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")
    check_request_data()
