#!/usr/bin/env python3
"""Decryption AES Implamatation."""
from util import make_phrase_xor, int_to_bit_array, adding_id_missing
from util import separe_keys_in_bytes, sub_phrase
import copy

def inv_shift_rows(shift):
     s = copy.copy(shift)

     s[1][1], s[2][1], s[3][1], s[0][1] = s[0][1], s[1][1], s[2][1], s[3][1]
     s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
     s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

     return s

def inv_mix_columns():
    pass

def inv_sub_bytes(phrase):
    phrase_sub = sub_phrase(phrase, 1)
    return phrase_sub

def add_round_cipher(plain, key):
    applied_key = make_phrase_xor(plain, key)
    return applied_key

def init_cipher_text(plain_int):
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


def decryption(text, expanded_key):
    text = init_cipher_text(text)
    initial_transformation = add_round_cipher(text, expanded_key[40:44])
    shift_text = inv_shift_rows(initial_transformation)
    inv_sub = inv_sub_bytes(shift_text)
    add_round = add_round_cipher(inv_sub, expanded_key[36:40])
    print(add_round)
