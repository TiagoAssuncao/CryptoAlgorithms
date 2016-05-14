#!/usr/bin/env python3
"""Decryption AES Implamatation."""

def inv_shift_rows():
    pass

def inv_mix_columns():
    pass

def inv_sub_bytes():
    pass

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


def decryption(text):
    text = init_cipher_text(text)
