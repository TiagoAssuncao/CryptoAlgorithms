#!/usr/bin/env python3

def rc4(key, plain):
    converted_key = convert_to_int(key)
    initilize = ksa(key)
    stream = prga(initilize)

    return stream
if __name__ == "__main__":
    key = "supersecretkey"
    plain = "plain"

    rc4(key, plain)
