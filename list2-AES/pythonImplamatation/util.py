#!/usr/bin/env python3
from sboxes import *

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

def array_bits_to_int(array):
    array_length = len(array)
    a = 0

    for i in reversed(range(0, array_length)):
        a += array[i] << i

    return a

def rot_word(word):
    word[0], word[1], word[2], word[3] = word[1], word[2], word[3], word[0]

    return word

def make_xor(first_word, second_word):
    word_xor_applied = []

    for i in range(0, 4):
        first_byte = first_word[i]
        second_byte = second_word[i]
        byte_xor_applied = []

        for j in range(0, 8):
            byte_xor_applied[j] = first_byte[j] ^ second_byte[j]

        word_xor_applied[i] = byte_xor_applied

    return word_xor_applied
