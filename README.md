# tg_spy_game

## English

Telegram bot for the "Spy" party game. Players create a room, join it with a short code, choose a character set, and start a round. The bot sends each participant their role or character in private messages.

### Features

- create a game room in Telegram;
- join a room by code;
- prevent one user from joining multiple rooms at the same time;
- room settings for the room creator;
- character set selection;
- two game modes: normal and chaos;
- start a new round without recreating the room;
- automatic role distribution to players.

### Project Structure

- `main.py` - entry point that creates `Bot`, `Dispatcher`, and starts polling;
- `Bot/handlers/` - command, callback button, and room flow handlers;
- `Bot/keyboards/` - Telegram inline keyboards;
- `Bot/servise/` - room and game state logic;
- `Bot/configs/` - room settings;
- `Game/` - game settings and role generation.

### Requirements

- Python 3.12 or newer;
- Telegram bot created through BotFather;
- dependencies from `requirements.txt`.

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Demochko-d/tg_spy_game.git
   cd tg_spy_game
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   For Linux/macOS:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your bot token:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   ```

### Run

Start the bot:

```bash
python main.py
```

After a successful start, the console will show:

```text
бот запущен
```

Then open the bot in Telegram and send `/start`.

### Gameplay

1. One player creates a room.
2. Other players enter the room code and join.
3. The room creator chooses the game settings.
4. When there are at least 3 players in the room, the creator starts the round.
5. The bot sends each player their role or character.
6. The creator can start a new round or delete the room.

### Environment Variables

| Variable | Description |
| --- | --- |
| `BOT_TOKEN` | Telegram bot token from BotFather |

### Dependencies

Main libraries:

- `aiogram` - Telegram Bot API framework;
- `python-dotenv` - loads environment variables from `.env`.

### Notes

- Room state is stored in process memory. After restarting the bot, all active rooms are reset.
- The `.env` file must not be committed to Git because it contains a secret token.

## Русский

Telegram-бот для игры "Шпион". Игроки создают комнату, подключаются к ней по короткому коду, выбирают набор персонажей и запускают партию. Бот раздает каждому участнику роль или персонажа в личные сообщения.

### Возможности

- создание игровой комнаты в Telegram;
- подключение игроков по коду комнаты;
- защита от повторного входа пользователя в разные комнаты;
- настройки комнаты для автора;
- выбор набора персонажей;
- два режима игры: обычный и хаос;
- запуск новой партии без пересоздания комнаты;
- автоматическая рассылка ролей игрокам.

### Структура проекта

- `main.py` - точка входа, создает `Bot`, `Dispatcher` и запускает polling;
- `Bot/handlers/` - обработчики команд, callback-кнопок и сценариев комнат;
- `Bot/keyboards/` - inline-клавиатуры Telegram;
- `Bot/servise/` - логика комнат и текущего состояния игры;
- `Bot/configs/` - настройки комнат;
- `Game/` - игровые настройки и генерация ролей.

### Требования

- Python 3.12 или новее;
- Telegram-бот, созданный через BotFather;
- зависимости из `requirements.txt`.

### Настройка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/Demochko-d/tg_spy_game.git
   cd tg_spy_game
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   Для Linux/macOS:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` в корне проекта и добавьте токен бота:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   ```

### Запуск

Запустите бота командой:

```bash
python main.py
```

После успешного запуска в консоли появится сообщение:

```text
бот запущен
```

Дальше откройте бота в Telegram и отправьте команду `/start`.

### Игровой процесс

1. Один игрок создает комнату.
2. Остальные игроки вводят код комнаты и подключаются.
3. Автор комнаты выбирает настройки игры.
4. Когда в комнате минимум 3 игрока, автор запускает партию.
5. Бот отправляет каждому игроку его роль или персонажа.
6. Автор может запустить новую партию или удалить комнату.

### Переменные окружения

| Переменная | Описание |
| --- | --- |
| `BOT_TOKEN` | Токен Telegram-бота от BotFather |

### Зависимости

Основные библиотеки:

- `aiogram` - Telegram Bot API framework;
- `python-dotenv` - загрузка переменных окружения из `.env`.

### Примечания

- Состояние комнат хранится в памяти процесса. После перезапуска бота все активные комнаты сбрасываются.
- Файл `.env` не должен попадать в Git, так как содержит секретный токен.
