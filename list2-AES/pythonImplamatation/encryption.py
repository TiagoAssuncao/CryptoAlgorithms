#!/usr/bin/env python3
"""Algorithm to encryption AES."""
from util import int_to_bit_array, adding_id_missing, separe_keys_in_bytes
def sub_bytes():
    pass

def shift_rows():
    pass

def mix_columns():
    pass

def add_round_plain():
    pass

def init_plain_text(plain_int):
    plain = int_to_bit_array(plain_int)
    plain = adding_id_missing(plain, 128)
    plain = separe_keys_in_bytes(plain)

    return plain

def encryption(plain_int):
   plain = init_plain_text(plain_int)