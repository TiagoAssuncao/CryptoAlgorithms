#!/usr/bin/env python3
"""Decryption AES Implamatation."""

def inv_shift_rows():
    pass

def inv_mix_columns():
    pass

def inv_sub_bytes(shift):
     s = copy.copy(shift)
     copy_0_3 = copy.copy(shift[0][3])
     copy_0_2 = copy.copy(shift[0][2])
     copy_1_3 = copy.copy(shift[1][3])
     copy_0_1 = copy.copy(shift[0][1])
     copy_1_2 = copy.copy(shift[1][2])
     copy_2_3 = copy.copy(shift[2][3])

     s[0][1], s[0][2], s[0][3] = shift[1][1], shift[2][2], shift[3][3]
     s[1][1], s[1][2], s[1][3] = shift[2][1], shift[3][2], copy_0_3
     s[2][1], s[2][2], s[2][3] = shift[3][1], copy_0_2, copy_1_3
     s[3][1], s[3][2], s[3][3] = copy_0_1, copy_1_2, copy_2_3
     return s


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
    shift_text = inv_shift_rows(text)
    initial_transformation = add_round_plain(plain, expanded_key[0:4])
