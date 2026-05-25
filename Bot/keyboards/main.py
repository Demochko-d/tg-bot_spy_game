from aiogram.types import InlineKeyboardMarkup

from Bot.keyboards.buttons import create_room_button, join_room_button, info_button


main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [create_room_button],
        [join_room_button],
        [info_button]
    ]
)
