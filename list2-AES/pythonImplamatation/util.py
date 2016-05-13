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

        int_number_sbox = SboxArray[left][rigth]
        array = int_to_bit_array(int_number_sbox)
        array = adding_id_missing(array, 8)

        sub_word_apply.append(array)

    return sub_word_apply

def get_word_numbers(word):
    word_in_numbers = []
    for i in range(4):
        word_in_numbers.append(array_bits_to_int(word[i]))

    return word_in_numbers

def mult_column(word):
    word_in_numbers = get_word_numbers(word)
    response = []

    for j in range(4):
        current_mix = MixState[j]
        mult_array = []

        for i in range(4):
            mult_array.append(mult_gf2_8(word_in_numbers[i], current_mix[i]))

        sum_result = mult_array[0]
        for i in range(1, 4):
            sum_result = sum_in_gf2_8(sum_result, mult_array[i])

        response.append(sum_result)

    response_array = []
    for i in range(4):
        response_array.append(adding_id_missing(int_to_bit_array(response[i]), 8))

    return response_array

def transform_to_int(text):
    word = []
    for i in range(4):
        current_word = text[i]
        current_word = mult_column(current_word)
        word.append(current_word)

    return word

def sub_phrase(phrase):
    phrase_sub = []

    for i in range(4):
        phrase_sub.append(sub_word(phrase[i]))

    return phrase_sub

def sum_in_gf2_8(a, b):
    c = a ^ b
    return c

def makeVectorMult(a):
    vmult = [a,0,0,0,0,0,0,0]
    for i in range(1, 8):
        var = vmult[i-1]
        if (var & 128) == 128:
            var = ((var - 128 )<< 1)
            var = var ^ 27
        else:
            var = var << 1

        vmult[i] = var

    return vmult

def getIndex(a):
    v = [1, 2, 4, 8, 16, 32, 64, 128]
    ids = []
    cont = 0

    for i in v:
        if(a & i) == i:
            ids.append(cont)

        cont = cont + 1
    return ids

def mult_gf2_8(a, b):
    vmult = makeVectorMult(a)
    ids = getIndex(b)
    values = []

    result = 0
    for i in ids:
        result = result ^ vmult[i]
    return result

def array_bits_to_int(array):
    array_length = len(array)
    a = 0

    for i in reversed(range(0, array_length)):
        a += array[array_length - i - 1] << i

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
        key_separed.append(key[i*8:i*8 + 8])

    return key_separed

def adding_id_missing(key, total_numbers):
    key_length = len(key)
    number_missing = total_numbers - key_length

    if number_missing != 0:
        for i in range(0, number_missing):
            key = insert_and_shift(key)

    return key


def int_to_bit_array(number):
    number_length = number.bit_length()
    bit_array = [(number & (1 << i)) >> i for i in reversed(range(number_length))]

    return bit_array

def apply_rcon(word, current_round):
    first_byte = word[0]
    rconj = Rcon[current_round]
    rconj_array = int_to_bit_array(rconj)
    rconj_array = adding_id_missing(rconj_array, 8)

    rcon_xor = make_byte_xor(first_byte, rconj_array)
    word[0] = rcon_xor

    return word

def make_byte_xor(first_byte, second_byte):
    byte_xor_applied = []

    for j in range(8):
        byte_xor_applied.append(first_byte[j] ^ second_byte[j])

    return byte_xor_applied

def make_word_xor(first_word, second_word):
    word_xor_applied = []

    for i in range(4):
        word_xor_applied.append(make_byte_xor(first_word[i], second_word[i]))

    return word_xor_applied

def make_phrase_xor(first_phrase, second_phrase):
    phrase_xor_applied = []

    for i in range(4):
        phrase_xor_applied.append(make_word_xor(
            first_phrase[i],
            second_phrase[i]
        ))

    return phrase_xor_applied
