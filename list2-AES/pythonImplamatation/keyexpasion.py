#!/usr/bin/env python3
from util import sub_word, rot_word, make_xor


def init_expanded_key(key):
    expanded_key = []

    for i in range(0, 4):
        expanded_key[i] = [
            key[4*i],
            key[4*i + 1],
            key[4*i + 2],
            key[4*i + 3]
        ]

    return expanded_key

def key_expasion(key):
    expanded_key = init_expanded_key(key)

    for i in range(4, 44):
        last_word = expanded_key[i - 1]

        expanded_key[i] = make_xor(
            expanded_key[i - 4],
            expanded_key[last_word]
        )