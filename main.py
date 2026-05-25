import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from Bot.handlers.setup_routers import setup_routers
from Bot.servise.Game import Game


load_dotenv()

async def main() -> None:

    bot = Bot(token=os.getenv("BOT_TOKEN"))

    game = Game()

    dispatcher = Dispatcher(game=game)

    setup_routers(dispatcher)

    print("бот запущен")

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
