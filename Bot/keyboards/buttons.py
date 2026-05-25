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
