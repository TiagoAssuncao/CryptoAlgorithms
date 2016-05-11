#!/usr/bin/env python3
"""Algorithm to encryption AES."""
from util import int_to_bit_array, adding_id_missing, separe_keys_in_bytes
from util import make_phrase_xor
def sub_bytes():
    pass

def shift_rows():
    pass

def mix_columns():
    pass

def add_round_plain(plain, key):
    applied_key = make_phrase_xor(plain, key)
    return applied_key

def init_plain_text(plain_int):
    plain_final = []

    plain = int_to_bit_array(plain_int)
    plain = adding_id_missing(plain, 128)
    plain = separe_keys_in_bytes(plain)

    for i in range(0, 4):
        plain_final.append([
            plain[4*i],
            plain[4*i + 1],
            plain[4*i + 2],
            plain[4*i + 3]
        ])

    return plain_final

def encryption(plain_int, expanded_key):
   plain = init_plain_text(plain_int)
   initial_transformation = add_round_plain(plain, expanded_key[0])
