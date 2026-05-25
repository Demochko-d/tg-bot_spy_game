from Bot.servise.Room import Room


class Game:

    AUTHOR_ROLE = "author"
    PLAYER_ROLE = "player"
    JOIN_SUCCESS = "success"
    JOIN_ROOM_NOT_FOUND = "room_not_found"
    JOIN_USER_ALREADY_IN_ROOM = "user_already_in_room"
    LEAVE_USER_NOT_IN_ROOM = "user_not_in_room"
    LEAVE_AUTHOR_MUST_DELETE_ROOM = "author_must_delete_room"

    def __init__(self):
        self.list_room = []
        self.rooms_by_id = {}
        self.rooms_by_key = {}
        self.used_keys = set()
        self.next_room_id = 1
        # user_id: None | room_key | "player"
        # Автор хранится по ключу комнаты, обычный игрок - по роли player.
        self.user_room = {}

    def new_room(self, author):
        if self.is_user_in_room(author):
            return None

        room = Room(self.next_room_id, author, self.used_keys)
        self.next_room_id += 1

        self.list_room.append(room)
        self.rooms_by_id[room.id] = room
        self.rooms_by_key[room.key] = room
        self.used_keys.add(room.key)

        self._save_user_room(author, room.key)

        return room

    def add_player_to_room(self, room_key, player):
        """Подключает игрока к комнате"""
        if self.is_user_in_room(player):
            return None, self.JOIN_USER_ALREADY_IN_ROOM

        room = self.get_room_by_key(room_key)

        if room is None:
            return None, self.JOIN_ROOM_NOT_FOUND

        room.new_player(player)
        self._save_user_room(player, self.PLAYER_ROLE)

        return room, self.JOIN_SUCCESS

    def leave_room(self, player):
        """Удаляет обычного игрока из комнаты."""
        room = self.get_user_room(player)

        if room is None:
            return None, self.LEAVE_USER_NOT_IN_ROOM

        if room.author.id == player.id:
            return room, self.LEAVE_AUTHOR_MUST_DELETE_ROOM

        room.delete_player(player)
        self.user_room.pop(player.id, None)

        return room, self.JOIN_SUCCESS

    def get_room_by_key(self, room_key):
        """Ищет комнату по ключу подключения."""
        normalized_key = room_key.strip().upper()
        return self.rooms_by_key.get(normalized_key)

    def get_room_by_id(self, room_id):
        """Ищет комнату по внутреннему id."""
        return self.rooms_by_id.get(room_id)

    def _save_user_room(self, user, role):
        """Записывает только роль пользователя в глобальный словарь."""
        self.user_room[user.id] = role

    def get_user_role(self, user):
        """Возвращает роль пользователя или None, если он не в комнате."""
        return self.user_room.get(user.id)

    def is_user_in_room(self, user):
        """Проверяет, состоит ли пользователь в какой-либо комнате."""
        return self.get_user_role(user) is not None

    def get_user_room(self, user):
        """Возвращает комнату пользователя, если он состоит в комнате."""
        role = self.get_user_role(user)

        if role is None:
            return None

        if role != self.PLAYER_ROLE:
            return self.get_room_by_key(role)

        for room in self.list_room:
            for player in room.list_players:
                if player.id == user.id:
                    return room

        return None

    def delete_room(self, room_key):
        """Удаляет комнату и очищает статусы всех ее участников."""
        room = self.get_room_by_key(room_key)

        if room is None:
            return None

        self.list_room = [
            current_room
            for current_room in self.list_room
            if current_room.id != room.id
        ]
        self.rooms_by_id.pop(room.id, None)
        self.rooms_by_key.pop(room.key, None)
        self.used_keys.discard(room.key)

        for player in room.list_players:
            self.user_room.pop(player.id, None)

        return room
