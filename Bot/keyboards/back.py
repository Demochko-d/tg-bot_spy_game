from aiogram.types import InlineKeyboardMarkup

from Bot.keyboards.buttons import back_button, logout_button


back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_button],
    ]
)
logout_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [logout_button],
    ]
)