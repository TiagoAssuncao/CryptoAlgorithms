#!/usr/bin/env python3

def prga(text):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + stream[i]) % 256
        stream[i], stream[j] = stream[j], stream[i]

        K = stream[(stream[i] + stream[j]) % 256]
        yield K

def ksa(key):
    length = key.__len__()
    stream = range(256)
    j=0

    for i in range(256):
        j = (j + stream[i] + key[i % length]) % 256
        stream[i], stream[j] = stream[j], stream[i]

    return stream

def convert_to_int(key):
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

    stream = rc4(key, plain)

    import sys
    for c in plain:
        sys.stdout.write("%02X" % (ord(c) ^ stream.next()))
    print
