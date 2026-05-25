from aiogram import F, Router
from aiogram.types import CallbackQuery

from Bot.keyboards.buttons import INFO_FOR_GAME
from Bot.keyboards.back import back_keyboard

router = Router()


@router.callback_query(F.data == INFO_FOR_GAME)
async def info_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Как играть в Шпиона:\n\n"
        "1. Создатель комнаты отправляет код остальным игрокам.\n"
        "2. Все участники подключаются по коду комнаты.\n"
        "3. После старта один игрок становится шпионом, остальные узнают локацию.\n"
        "4. Игроки задают друг другу вопросы и пытаются вычислить шпиона.\n"
        "5. Шпион старается понять локацию и не выдать себя.",
        reply_markup=back_keyboard,
    )
    await callback.answer()
