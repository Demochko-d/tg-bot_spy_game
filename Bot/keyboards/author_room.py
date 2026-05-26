from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Bot.keyboards.buttons import (
    SET_CHARACTER_SET_PREFIX,
    SET_GAME_MODE_PREFIX,
    back_to_room_menu_button,
    change_modes,
    delete_room_button,
    settings_button,
    show_sets,
    start_button,
)
from Game.game_config.game_config import character_sets, game_modes


author_room_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [start_button],
        [settings_button],
        [delete_room_button],
    ]
)

settings_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [show_sets],
        [change_modes],
        [back_to_room_menu_button],
    ]
)


def get_character_sets_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=character_set,
                    callback_data=f"{SET_CHARACTER_SET_PREFIX}{character_set}",
                )
            ]
            for character_set in character_sets
        ] + [[back_to_room_menu_button]]
    )


def get_game_modes_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=mode,
                    callback_data=f"{SET_GAME_MODE_PREFIX}{mode}",
                )
            ]
            for mode in game_modes
        ] + [[back_to_room_menu_button]]
    )
