import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DB_PATH = "C:/Users/proni/PycharmProjects/python_basic_diploma/database/database.db"
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Вывести минимальный коэффициент"),
    ("high", "Вывести максимальный коэффициент"),
    ("custom", "Вывести указанный диапазон коэффициент"),
    ("history", "Вывести последние 10 запросов"),
)
