from aiogram.types import InlineKeyboardMarkup

from Bot.keyboards.buttons import settings_button, delete_room_button, start_button


author_room_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [start_button],
        [settings_button],
        [delete_room_button],
    ]
)
