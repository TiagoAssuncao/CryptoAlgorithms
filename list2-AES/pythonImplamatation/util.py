#!/usr/bin/env python3
import sboxes

Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

def sub_word(word):
    sub_word_apply = []

    for i in range(0, 4):
        current_byte = word[i]
        left = array_bits_to_int(current_byte[0:4])
        rigth = array_bits_to_int(current_byte[4:8])

        sub_word_apply[i] = Sbox[left][rigth]

    return sub_word_apply

def rot_word(word):
    word[0], word[1], word[2], word[3] = word[1], word[2], word[3], word[0]

    return word
