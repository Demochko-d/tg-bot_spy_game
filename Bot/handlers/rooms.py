from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from Bot.keyboards.buttons import CREATE_ROOM_CALLBACK, JOIN_ROOM_CALLBACK, INPUT_KEY_FOR_ROOM
from Bot.servise.Game import Game
from Bot.keyboards.author_room import author_room_keyboard
from Bot.keyboards.back import back_keyboard
from Bot.keyboards.error_key import error_keyboard
from Bot.keyboards.player_room import player_room_keyboard

router = Router()


class JoinRoomState(StatesGroup):
    waiting_for_room_tag = State()


def get_players_text(players):
    return "\n".join(
        f"- {player.full_name}"
        for player in players
    )


@router.callback_query(F.data == CREATE_ROOM_CALLBACK)
async def create_room_handler(callback: CallbackQuery, game: Game):
    room = game.new_room(author=callback.from_user)

    if room is None:
        await callback.message.edit_text("Вы уже состоите в комнате.")
        await callback.answer()
        return

    await callback.message.edit_text(
        f"Комната {room.id} создана.\n"
        f"Автор: {callback.from_user.full_name}\n"
        f"Код комнаты: {room.key}\n\n"
        f"Набор персонажей: {room.character_set}\n"
        f"Режим: {room.mode}\n\n"
        f"Список участников:\n{get_players_text(room.list_players)}",
        reply_markup=author_room_keyboard,
    )

    await callback.answer()


@router.callback_query(F.data == JOIN_ROOM_CALLBACK)
async def join_room_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(JoinRoomState.waiting_for_room_tag)

    if callback.message:
        await callback.message.edit_text(
            "Введите код комнаты, его нужно узнать у создателя комнаты:",
            reply_markup=back_keyboard)

    await callback.answer()


@router.message(JoinRoomState.waiting_for_room_tag)
async def process_room_tag(
    message: Message,
    state: FSMContext,
    game: Game,
    bot: Bot,
):
    room_tag = message.text.strip().upper()
    room, join_status = game.add_player_to_room(room_tag, message.from_user)

    if join_status == game.JOIN_USER_ALREADY_IN_ROOM:
        await message.answer("Вы уже состоите в комнате.",
                             reply_markup=back_keyboard)
        await state.clear()
        return

    if join_status == game.JOIN_ROOM_NOT_FOUND:
        await message.answer("Неверный код комнаты, попробуйте ещё раз. \n"
                             "Введите код комнаты:",
                             reply_markup=error_keyboard)
        return

    players_text = get_players_text(room.list_players)


    for player in room.list_players[:-1:]:
        await bot.send_message(
            chat_id=player.id,
            text=(
                f"Игрок {message.from_user.full_name} подключился к комнате.\n\n"
            )
        )
    await bot.send_message(
        chat_id=room.list_players[-1].id,
        text=(f"Вы подключились к комнате {room.id}!\n\n"
            f"Автор: {room.author.full_name}\n"
            f"Набор персонажей: {room.character_set}\n"
            f"Режим: {room.mode}\n"
            f"Список участников:\n{players_text}"
        ),
        reply_markup=player_room_keyboard,
    )

    await state.clear()


@router.callback_query(F.data == INPUT_KEY_FOR_ROOM)
async def retry_input_room_key(
    callback: CallbackQuery,
    state: FSMContext,
):

    await state.set_state(JoinRoomState.waiting_for_room_tag)

    await callback.message.edit_text(
        "Введите код комнаты:"
    )

    await callback.answer()
