from Game.game_config.game_config import character_sets, NORMAL_MODE, CHAOS_MODE

import random

SPY = 'Шпион'

chance_to_normal = 60
chance_to_rng_characters_all = 20
chance_to_all_spy = 100 - chance_to_normal - chance_to_rng_characters_all

def get_rng_character_list_normal(len_list, set_ch):

    characters = [random.choice(character_sets[set_ch])] * len_list
    spy = random.randint(0, len_list - 1)
    characters[spy] = SPY
    return characters


def get_rng_character_list_chaos(len_list, set_ch):

    mode_in_chaos = random.randint(1, 100)

    if mode_in_chaos <= chance_to_normal:
        characters = get_rng_character_list_normal(len_list, set_ch)

    elif mode_in_chaos <= chance_to_rng_characters_all + chance_to_normal:
        characters = [random.choice(character_sets[set_ch]) for _ in range(len_list)]

    else:
        characters = [SPY for _ in range(len_list)]

    return characters


def shoise_charter_list(len_list_players, mode, character_set):

    if mode == NORMAL_MODE:
        list_for_players = get_rng_character_list_normal(len_list_players, character_set)
    else:
        list_for_players = get_rng_character_list_chaos(len_list_players, character_set)

    return list_for_players