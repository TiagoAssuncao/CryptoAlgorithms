#!/usr/bin/env python3
from util import sub_word, rot_word, make_word_xor, apply_rcon, int_to_bit_array
from util import adding_id_missing, separe_keys_in_bytes

def init_expanded_key(key_int):
    expanded_key = []
    key = int_to_bit_array(key_int)
    key_length = len(key)
    key = adding_id_missing(key, key_length)
    key = separe_keys_in_bytes(key)

    for i in range(0, 4):
        expanded_key.append([
            key[4*i],
            key[4*i + 1],
            key[4*i + 2],
            key[4*i + 3]
        ])

    return expanded_key

def apply_fuction_g(last_word, current_round):
    last_word = rot_word(last_word)
    last_word = sub_word(last_word)
    print(last_word)
    last_word = apply_rcon(last_word, current_round)

    return last_word

def key_expansion(key):
    expanded_key = init_expanded_key(key)

    for i in range(4, 44):
        last_word = expanded_key[i - 1]

        if (i%4) == 0:
            current_round = int(i/4)
            last_word = apply_fuction_g(last_word, current_round)

        expanded_key[i] = make_word_xor(
            expanded_key[i - 4],
            last_word
        )

    return expanded_key
