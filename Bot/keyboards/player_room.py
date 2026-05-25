from aiogram.types import InlineKeyboardMarkup

from Bot.keyboards.buttons import logout_button


player_room_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [logout_button],
    ]
)
