from aiogram.types import InlineKeyboardMarkup

from Bot.keyboards.buttons import back_button


error_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_button],
    ]
)
