#!/usr/bin/env python3

def converted_key(key):
    converted_key = []
    for i in key:
        converted_key.append(ord(i))

    return converted_key

def rc4(key, plain):
    converted_key = convert_to_int(key)
    initilize = ksa(key)
    stream = prga(initilize)

    return stream
if __name__ == "__main__":
    key = "supersecretkey"
    plain = "plain"

    rc4(key, plain)
