from aiogram import Dispatcher

from Bot.handlers.detal_room import router as detal_room_router
from Bot.handlers.info import router as info_router
from Bot.handlers.rooms import router as rooms_router
from Bot.handlers.start import router as start_router


def setup_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(start_router)
    dispatcher.include_router(rooms_router)
    dispatcher.include_router(detal_room_router)
    dispatcher.include_router(info_router)
