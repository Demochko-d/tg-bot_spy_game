from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery

from Bot.configs import room_config
from Bot.keyboards.buttons import (
    BACK_TO_ROOM_MENU,
    CHANGE_MODES,
    DELETE_KEY_FOR_ROOM,
    LEAVE_ROOM_CALLBACK,
    SET_CHARACTER_SET_PREFIX,
    SET_GAME_MODE_PREFIX,
    SHOW_SETS,
    START_GAME,
    SETTINGS_FOR_GAME,
)
from Bot.keyboards.game_process import admin_game_keyboard, player_game_keyboard
from Bot.keyboards.main import main_keyboard
from Bot.keyboards.author_room import (
    author_room_keyboard,
    get_character_sets_keyboard,
    get_game_modes_keyboard,
    settings_keyboard,
)
from Bot.servise.Game import Game
from Game.game_config.game_config import character_sets, game_modes
from Game.service.shoise_charter import shoise_charter_list

router = Router()


@router.callback_query(F.data == DELETE_KEY_FOR_ROOM)
async def delete_room_handler(callback: CallbackQuery, game: Game, bot: Bot):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Удалить комнату может только автор.", show_alert=True)
        return

    deleted_room = game.delete_room(room.key)

    if deleted_room is None:
        await callback.answer("Комната уже удалена.", show_alert=True)
        return

    for player in deleted_room.list_players:
        if player.id == callback.from_user.id:
            continue

        await bot.send_message(
            chat_id=player.id,
            text=(
                "Автор комнаты удалил ее.\n\n"
                "Вы перемещены в главное меню. Выберите действие, чтобы начать игру:"
            ),
            reply_markup=main_keyboard,
        )

    if callback.message:
        await callback.message.edit_text(
            "Комната удалена. Вы перемещены в главное меню.\n\n"
            "Выберите действие, чтобы начать игру:",
            reply_markup=main_keyboard,
        )

    await callback.answer()


@router.callback_query(F.data == LEAVE_ROOM_CALLBACK)
async def leave_room_handler(callback: CallbackQuery, game: Game, bot: Bot):
    player = callback.from_user
    room, leave_status = game.leave_room(player)

    if leave_status == game.LEAVE_USER_NOT_IN_ROOM:
        await callback.answer("Вы не состоите в комнате.", show_alert=True)
        return

    if leave_status == game.LEAVE_AUTHOR_MUST_DELETE_ROOM:
        await callback.answer(
            "Автор не может выйти из комнаты. Удалите комнату.",
            show_alert=True,
        )
        return

    for current_player in room.list_players:
        await bot.send_message(
            chat_id=current_player.id,
            text=(
                f"Игрок {player.full_name} вышел из комнаты.\n\n"
            ),
        )

    if callback.message:
        await callback.message.edit_text(
            "Вы вышли из комнаты.\n\n"
            "Выберите действие, чтобы начать игру:",
            reply_markup=main_keyboard,
        )

    await callback.answer()


@router.callback_query(F.data == START_GAME)
async def start_game_handler(callback: CallbackQuery, game: Game, bot: Bot):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Начать игру может только автор комнаты.", show_alert=True)
        return


    players_count = len(room.list_players)

    if players_count < room_config.min_players_for_game:
        await callback.answer(
            (
                "Недостаточно игроков для старта. "
                f"Нужно минимум: {room_config.min_players_for_game}. "
                f"Сейчас: {players_count}."
            ),
            show_alert=True,
        )
        return

    room.restart_game()

    list_for_playrs = shoise_charter_list(len(room.list_players), room.mode, room.character_set)

    for current_player in room.list_players:
        turn_number = room.get_turn_number(current_player)
        is_author = current_player.id == room.author.id
        keyboard = admin_game_keyboard if is_author else player_game_keyboard
        greeting = "Вы начали игру!" if is_author else "Игра началась!"
        text = (
            f"{greeting}\n\n"
            f"Партия: {room.game_number}\n"
            f"Ваш персоонаж: {list_for_playrs[turn_number - 1]}. \n\n"
            f"Набор персонажей: {room.character_set}\n"
            f"Режим: {room.mode}\n"
            f"Ваш номер хода: {turn_number}"
        )
        game_message_id = room.game_message_ids.get(current_player.id)

        if game_message_id is None:
            message = await bot.send_message(
                chat_id=current_player.id,
                text=text,
                reply_markup=keyboard,
            )
            room.game_message_ids[current_player.id] = message.message_id
        else:
            await bot.edit_message_text(
                chat_id=current_player.id,
                message_id=game_message_id,
                text=text,
                reply_markup=keyboard,
            )

    if callback.message and callback.message.message_id not in room.game_message_ids.values():
        await callback.message.edit_reply_markup(reply_markup=None)

    await callback.answer()


@router.callback_query(F.data == SETTINGS_FOR_GAME)
async def game_placeholder_handler(callback: CallbackQuery, game: Game, bot: Bot):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Настраивать комнату может только автор.", show_alert=True)
        return

    await callback.message.edit_text(
        (
            "Настройки комнаты.\n\n"
            f"Набор персонажей: {room.character_set}\n"
            f"Режим: {room.mode}"
        ),
        reply_markup=settings_keyboard
    )

    await callback.answer()


@router.callback_query(F.data == BACK_TO_ROOM_MENU)
async def back_to_room_menu_handler(callback: CallbackQuery, game: Game):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Вернуться в меню комнаты может только автор.", show_alert=True)
        return

    await callback.message.edit_text(
        (
            f"Комната {room.id}.\n"
            f"Автор: {room.author.full_name}\n"
            f"Код комнаты: {room.key}\n\n"
            f"Набор персонажей: {room.character_set}\n"
            f"Режим: {room.mode}"
        ),
        reply_markup=author_room_keyboard,
    )

    await callback.answer()


@router.callback_query(F.data == SHOW_SETS)
async def show_character_sets_handler(callback: CallbackQuery, game: Game):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Настраивать набор может только автор.", show_alert=True)
        return

    await callback.message.edit_text(
        "Выберите набор персонажей:",
        reply_markup=get_character_sets_keyboard(),
    )

    await callback.answer()


@router.callback_query(F.data == CHANGE_MODES)
async def show_game_modes_handler(callback: CallbackQuery, game: Game):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Настраивать режим может только автор.", show_alert=True)
        return

    await callback.message.edit_text(
        "Выберите режим игры:",
        reply_markup=get_game_modes_keyboard(),
    )

    await callback.answer()


@router.callback_query(F.data.startswith(SET_CHARACTER_SET_PREFIX))
async def set_character_set_handler(callback: CallbackQuery, game: Game):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Настраивать набор может только автор.", show_alert=True)
        return

    character_set = callback.data.removeprefix(SET_CHARACTER_SET_PREFIX)

    if character_set not in character_sets:
        await callback.answer("Такого набора персонажей нет.", show_alert=True)
        return

    room.set_character_set(character_set)

    await callback.message.edit_text(
        (
            "Набор персонажей изменен.\n\n"
            f"Текущий набор: {room.character_set}\n"
            f"Текущий режим: {room.mode}"
        ),
        reply_markup=settings_keyboard,
    )

    await callback.answer()


@router.callback_query(F.data.startswith(SET_GAME_MODE_PREFIX))
async def set_game_mode_handler(callback: CallbackQuery, game: Game):
    room = game.get_user_room(callback.from_user)

    if room is None or room.author.id != callback.from_user.id:
        await callback.answer("Настраивать режим может только автор.", show_alert=True)
        return

    mode = callback.data.removeprefix(SET_GAME_MODE_PREFIX)

    if mode not in game_modes:
        await callback.answer("Такого режима игры нет.", show_alert=True)
        return

    room.set_mode(mode)

    await callback.message.edit_text(
        (
            "Режим игры изменен.\n\n"
            f"Текущий набор: {room.character_set}\n"
            f"Текущий режим: {room.mode}"
        ),
        reply_markup=settings_keyboard,
    )

    await callback.answer()
