#!/usr/bin/env python3
"""Algorithm to encryption AES."""
from util import int_to_bit_array, adding_id_missing, separe_keys_in_bytes
from util import make_phrase_xor, sub_phrase, transform_to_int
from util import convert_text_in_number
import copy

def sub_bytes(phrase):
    phrase_sub = sub_phrase(phrase, 0)
    return phrase_sub

def shift_rows(shift):
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

def mix_columns(text):
    text = transform_to_int(text, 0)
    return text

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

def do_round(text, key, current_round):
   sub_byte = sub_bytes(text)
   shift = shift_rows(sub_byte)

   if current_round != 10:
       mixied = mix_columns(shift)
   else:
       mixied = shift

   add_round_key = add_round_plain(mixied, key)

   return add_round_key

def encryption(plain_int, expanded_key):
   plain = init_plain_text(plain_int)
   initial_transformation = add_round_plain(plain, expanded_key[0:4])
   text = initial_transformation

   for i in range(1, 11):
      text = do_round(text, expanded_key[i*4:i*4 + 4], i)

   text = convert_text_in_number(text)
   return text
