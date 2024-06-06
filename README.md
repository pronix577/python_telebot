# *Python Telegram Bot Api*
Этот Telegram-bot предназначен для взаимодействия с API ставок на хоккей лиги NHL.
Этот README предоставляет исчерпывающее руководство по использованию Telegram-бота,
предназначенного для получения коэффициентов ставок и взаимодействия с ними на основе команд пользователя.
Бот поддерживает несколько команд, позволяющих пользователям запрашивать минимальные и максимальные коэффициенты,
запрашивать данные в пользовательском диапазоне и просматривать историю своих запросов.
Проект состоит из нескольких функциональных слоёв: скрипта main.py, модуля,
отвечающего за работу с Telegram, модуля, отвечающего за работу с API стороннего
сайта, и модуля, работающего с БД.
*Все запросы к базе данных выполняются с помощью ORM Peewee*

## Сторонний функционал
1. python-dotenv~=1.0.1
    Для хранения BOT-Token и API-key
2. pyTelegramBotAPI==4.16.1
    Для работы с ботом
3. requests~=2.31.0
    Для запросов в json
4. peewee~=3.17.1
    Для работы с БД SQLite

## *Приступая к работе*
Чтобы начать взаимодействие с ботом, сначала убедитесь, что на вашем устройстве установлен Telegram.

## *Запуск бота*
-Клонирование репозитория
-Установка необходимых библиотек(pip install -r requirements.txt)
-Запуск скрипта main.py

## *Описание работы команд*
Бот поддерживает следующие команды:

### *Нестандартные команды*

1. *Команда /low*
Выводит минимальный коэффициент
После ввода команды пользователем выводится:
- Матч
- Команды: домашняя и гостева
- Название букмекера
- Самый низкий коэффициент
- 
Описание работы кода:
-Вначале идет проверка, зарегистрирован ли пользователь, если нет, то предлагается ввести команду /start
-Далее выводится пользователю сообщение "Вывожу минимальный коэффициент"
-Идет запрос к таблице Games БД
-Таблица сортирует по коэффициенту от меньшего к большему
-Выводится первое значение(оно же минимальное)
-Вызывается функция для логирование запроса

2. *Команда /high*
Выводит максимальный коэффициент
После ввода команды пользователем выводится:
- Матч
- Команды: домашняя и гостева
- Название букмекера
- Самый высокий коэффициент

Описание работы кода:
-Вначале идет проверка, зарегистрирован ли пользователь, если нет, то предлагается ввести команду /start
-Далее выводится пользователю сообщение "Вывожу максимальный коэффициент"
-Идет запрос к таблице Games БД
-Таблица сортирует по коэффициенту от большего к меньшему
-Выводится первое значение(оно же максимальное)
-Вызывается функция для логирование запроса

3. *Команда /custom*
Выводит коэффициент в указанном диапазоне
После ввода команды пользователем выводится:
- Матч
- Команды: домашняя и гостева
- Название букмекера
- Коэффициент в указанном диапазоне

Описание работы кода:
-Вначале идет проверка, зарегистрирован ли пользователь, если нет, то предлагается ввести команду /start
-Далее выводится пользователю сообщение "Вывести коэффициент в диапазоне от и до"
-Запрашивается у пользователя два значения через пробел сообщение: "Введите ОТ какого числа и ДО какого числа, через ПРОБЕЛ"
-Идет запрос к таблице Games БД
-Таблица сортирует по коэффициенту от большего к меньшему
-Переводит в состояние запроса диапазона
-Выводится результат
-Вызывается функция для логирование запроса

4. *Команда /history*
Выводит историю запросов
После ввода команды пользователем выводится:
- Команда
- Команды: домашняя и гостева
- Название букмекера
- Результат работы команды

Описание работы кода:
-Вначале идет проверка, зарегистрирован ли пользователь, если нет, то предлагается ввести команду /start
-Идет запрос к таблице History БД
-Таблица сортирует по времени запроса и id пользователя, запрашиваются последние 10
-Результат запроса к БД сохраняется в список
-Проверяется, пуст ли список
-Если список пуст выводится сообщение "У вас ещё нет запросов"
-В противном случае выводиться результат запроса к БД

### *Стандартные команды*

1. *Команда /start*
Начало работы с ботом
Также бот реагирует на текст "Привет"
После ввода команды пользователем выводится:
- Приветствие
Описание работы кода:
-Вначале с помощью конструкции try/except идет попытка создание пользователя в таблице User БД
-Если пользователь уже есть в БД, выводится: "Рад вас снова видеть, {имя пользователя}"
-Если пользователя нет в БД, выводится: "Добро пожаловать в букмекер!"
-Запрос к базе данных на обновление данных с API сайта.

2. *Команда /help*
Выводит команды и их краткое описание
-Запрашивает в config.py стандартные команды
-Циклом вывод название команды и их краткое описание

3. *Команда /echo*
Повторяет текст пользователя
-Если бот не в процессе выполнения команды повторяет сообщение

## *Работа с БД*
В данном боте используется база данных SQlite.
Работа осуществляется с помощью ORM Peewee
В файле models.py описаны следующие модели
Также, создаются указанные модели

1. User
Хранятся данные пользователя:
-ID пользователя(создается уникальный)
-Имя пользователя
-Ник пользователя
-Фамилия пользователя(если есть)

2. Games
Хранятся данные об играх.
-ID игры
-Время запроса
-Домашняя команда
-Гостевая команда
-Название букмекера
-На кого или что ставка
-Коэффициент

3. History
Хранит истории запросов пользователей
-ID запроса(создается автоматически)
-Ссылка на пользователя
-Имя пользователя
-Время запроса
-Название команды
-Результат выполнения команды


## *Работа с состояниями*
В данном проекте реализованно одно состояние - ввода диапазона чисел команды /custom

Описание работы:
-Проверка вводимых данных
-Запрос к БД с помощью between
-Если удалось найти значение, вывести их
-В противном случает вывести "Не удалось найти"
-Логировать запрос

## *Вспомогательные утилиты*
### *Проверка актуальности данных*
В файле check_data.py реализованна функция check_request_data()
В ней проводится проверка актуальности коэффициентов
Если с последнего запроса данных с API сайта прошло больше одного часа или данных нет, 
удалить прошлые данные, заново запросит новые данные
после вызывается функция записи

### *Запись в БД*
В файле write_db.py реализованна функция writing_to_db()
В ней храниться:
-URL
-Параметры запроса
-API Host
-API Key
-Путь к базе данных созданный с помощью библиотеки OS

Порядок записи:
-С помощью request делается API запрос
-Результаты сохраняются в JSON файл
-Считываются из JSON файла
-Записываются циклом в БД

### *Логирование запросов*
В файле log_request.py функция log_request() логирует запросы пользователя.
В функцию передаются:
-ID пользователя
-Имя пользователя
-Название команды
-Результат выполнения команды

Создается таблица History и вносятся данные:
-ID пользователя
-Имя пользователя
-Время запроса(текущие время)
-Название команды
-Результат выполнения команды