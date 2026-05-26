from aiogram.types import InlineKeyboardButton


CREATE_ROOM_CALLBACK = "create_room"
JOIN_ROOM_CALLBACK = "join_room"
BACK_TO_MAIN_MENU = "back_to_main_menu"
INFO_FOR_GAME = "info"
INPUT_KEY_FOR_ROOM = "input_key"
DELETE_KEY_FOR_ROOM = "delete_room"
START_GAME = "start_game"
SETTINGS_FOR_GAME = "settings_game"
LEAVE_ROOM_CALLBACK = "leave_room"
LEAVE_GAME_CALLBACK = "leave_game"
END_GAME = "end_game"
NEXT_GAME = "next_game"
SHOW_SETS = "show_sets"
CHANGE_MODES = "change_modes"
BACK_TO_ROOM_MENU = "back_to_room_menu"
SET_CHARACTER_SET_PREFIX = "set_character_set:"
SET_GAME_MODE_PREFIX = "set_game_mode:"

create_room_button = InlineKeyboardButton(
    text="Создать комнату",
    callback_data=CREATE_ROOM_CALLBACK,
)
join_room_button = InlineKeyboardButton(
    text="Вступить",
    callback_data=JOIN_ROOM_CALLBACK,
)
back_button = InlineKeyboardButton(
    text="Назад",
    callback_data=BACK_TO_MAIN_MENU,
)
logout_button = InlineKeyboardButton(
    text="Выйти из комнаты",
    callback_data=LEAVE_ROOM_CALLBACK,
)
info_button = InlineKeyboardButton(
    text="Как играть?",
    callback_data=INFO_FOR_GAME,
)
input_button = InlineKeyboardButton(
    text="Попробовать снова",
    callback_data=INPUT_KEY_FOR_ROOM,
)
delete_room_button = InlineKeyboardButton(
    text="Удалить комнату",
    callback_data=DELETE_KEY_FOR_ROOM,
)
start_button = InlineKeyboardButton(
    text="Начать игру",
    callback_data=START_GAME,
)
settings_button = InlineKeyboardButton(
    text="Настройки комнаты",
    callback_data=SETTINGS_FOR_GAME,
)
admin_game_end = InlineKeyboardButton(
    text="Завершить игру",
    callback_data=DELETE_KEY_FOR_ROOM,
)
admin_next_game = InlineKeyboardButton(
    text="Новая игра",
    callback_data=START_GAME,
)
player_game_leave = InlineKeyboardButton(
    text="Покинуть игру",
    callback_data=LEAVE_ROOM_CALLBACK,
)
show_sets = InlineKeyboardButton(
    text="Изменить набор персоонажей",
    callback_data=SHOW_SETS
)
change_modes = InlineKeyboardButton(
    text="Изменить режим",
    callback_data=CHANGE_MODES
)
back_to_room_menu_button = InlineKeyboardButton(
    text="Назад",
    callback_data=BACK_TO_ROOM_MENU,
)
