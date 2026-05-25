import random

from Bot.configs import room_config
from Game.game_config import game_config


def gen_key(used_keys):
    """Генерирует свободный код комнаты без повторов."""
    max_keys_count = len(room_config.alfabet) ** room_config.len_key

    if len(used_keys) >= max_keys_count:
        raise RuntimeError("Закончились свободные коды комнат.")

    while True:
        key = ''.join([
            random.choice(room_config.alfabet)
            for _ in range(room_config.len_key)
        ])

        if key not in used_keys:
            return key


class Room:

    def __init__(self, room_id, author, used_keys):
        self.id = room_id
        self.author = author
        self.list_players = [author]
        self.key = gen_key(used_keys)
        self.character_set = game_config.default_character_set
        self.mode = game_config.default_game_mode

    def new_player(self, player):
        """Добавляет игрока в комнату, если его там еще нет."""
        if player.id not in [p.id for p in self.list_players]:
            self.list_players.append(player)

        return self.list_players

    def delete_player(self, player):
        """Удаляет игрока из комнаты, если он там есть."""
        players_count = len(self.list_players)
        self.list_players = [
            current_player
            for current_player in self.list_players
            if current_player.id != player.id
        ]

        return len(self.list_players) != players_count
