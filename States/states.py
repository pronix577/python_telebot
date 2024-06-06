from telebot.handler_backends import State, StatesGroup
from telebot.types import Message
from loader import bot
from database.models import Games
from utils.misc.log_request import log_request


class UserState(StatesGroup):
    custom_val = State()


@bot.message_handler(state=UserState.custom_val)
def process_from_custom(message: Message) -> None:
    numbers = message.text.split()
    if len(numbers) > 2:
        bot.send_message(message.from_user.id, "Вы ввели больше двух значений")
        return
    try:
        from_num = int(numbers[0])
        to_num = int(numbers[1])
    except (ValueError, IndexError):
        bot.send_message(
            message.from_user.id, "Одно или два значений не являются числами"
        )
        return

    games_in_range = Games.select().where(Games.price.between(numbers[0], numbers[1]))
    if games_in_range:
        for i_range in games_in_range:
            bot.send_message(
                message.from_user.id,
                f"Домашняя команда - {i_range.home_team}\n"
                f"Гостевая команда - {i_range.away_team}\n"
                f"Букмекер - {i_range.title}\n"
                f"Коэффициент на {i_range.name_team} - {i_range.price}",
            )
    else:
        bot.send_message(
            message.from_user.id,
            "Не удалось найти коэффициентов в указанном диапазоне!",
        )
    result = f"Найдено совпадений {len(games_in_range)}"
    log_request(message.from_user.id, message.from_user.first_name, "/custom", result)
    bot.delete_state(message.from_user.id)
