from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import CallbackQuery

from Bot.keyboards.main import main_keyboard
from Bot.keyboards.buttons import BACK_TO_MAIN_MENU

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()

    await message.answer(
        "Добро пожаловать в игру Шпион!\n\n"
        "Выберите действие, чтобы начать игру:",
        reply_markup=main_keyboard,
    )


@router.callback_query(F.data == BACK_TO_MAIN_MENU)
async def back_to_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()

    if callback.message:
        await callback.message.edit_text(
            "Это главное меню игры Шпион!\n\n"
            "Выберите действие, чтобы начать игру:",
            reply_markup=main_keyboard,
        )

    await callback.answer()
