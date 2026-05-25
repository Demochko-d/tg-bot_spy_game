from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery

from Bot.configs import room_config
from Bot.keyboards.author_room import author_room_keyboard
from Bot.keyboards.buttons import DELETE_KEY_FOR_ROOM, LEAVE_ROOM_CALLBACK, START_GAME
from Bot.keyboards.main import main_keyboard
from Bot.servise.Game import Game


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

    for current_player in room.list_players:
        await callback.message.edit_text(
            "Игра началась!"
            f"Набор персонажей: {room.character_set}\n",
            f"Режим: {room.mode}",
            reply_markup=main_keyboard,
        )
        deleted_room = game.delete_room(room.key)

    if callback.message:
        await callback.message.edit_reply_markup(reply_markup=author_room_keyboard)

    await callback.answer()
