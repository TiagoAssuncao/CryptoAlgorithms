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

def insert_and_shift(key):
    """Adding value 0 in a position 0"""
    key.insert(0, 0)
    return key

def separe_keys_in_bytes(key):
    key_separed = []
    for i in range(0, 16):
        key_separed[i] = key[i*8:i*8 + 8]

    return key_separed

def adding_id_missing(key):
    key_length = len(key)
    number_missing = 128 - key_length

    if number_missing != 0:
        for i in range(0, number_missing):
            key = insert_and_shift(key)

    return key

def make_word_xor(first_word, second_word):
    word_xor_applied = []

    for i in range(0, 4):
        word_xor_applied[i] = make_byte_xor(first_word[i], second_word[i])

    return word_xor_applied

def int_to_bit_array(number):
    number_length = number.bit_length()
    bit_array = [(number & (1 << i)) >> i for i in reversed(range(number_length))]

    return bit_array

def apply_rcon(word, current_round):
    first_byte = word[0]
    rconj = Rcon[current_round]
    rconj_array = int_to_bit_array(rconj)

    rcon_xor = make_byte_xor(first_byte, rconj_array)
    word[0] = rcon_xor

    return word

def make_byte_xor(first_byte, second_byte):
    byte_xor_applied = []

    for j in range(0, 8):
        byte_xor_applied[j] = first_byte[j] ^ second_byte[j]

    return byte_xor_applied
