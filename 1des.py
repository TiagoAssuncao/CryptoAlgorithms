"""DES implementation"""
import numpy

numberKeys = 6
keys = [[0 for x in range(8)] for x in range(numberKeys)]
plain_text_length = 8

def swap_keys(roundpack):
    return roundpack[1], roundpack[0]

def makeLists(arg, length):
    arglist = [(arg & (1 << i)) >> i for i in reversed(range(length))]
    return arglist

def makeKeys(key):
    key = key & 0b0011111111
    keyList = makeLists(key, 8)
    for i in range(0, numberKeys):
        subkey = [None]*8
        subkey[0:7] = keyList[1:8]
        subkey[7] = keyList[0]
        keys[i] = subkey
        keyList = subkey

def appfuction(roundpack, current_round):
    rigth_text = roundpack[1]

    add_round_key = [0]*int(plain_text_length/2)
    current_key = keys[current_round]

    for i in rigth_text:
        add_round_key[i] = rigth_text[i] ^ current_key[i]

    return add_round_key

def doRound(roundpack, current_round):
    final_left_text = roundpack[1]
    left_text = roundpack[0]

    rigth_text_fuction = appfuction(roundpack, current_round)
    final_rigth_text = [0]*int(plain_text_length/2)

    for i in rigth_text_fuction:
        final_rigth_text[i] = rigth_text_fuction[i] ^ left_text[i]

    print(current_round, ": ", final_left_text, final_rigth_text)
    return final_left_text, final_rigth_text

def make_round_pack(plain_text_list):
    rigth_text = [None]*(int(plain_text_length/2))
    left_text = [None]*(int(plain_text_length/2))

    rigth_text = plain_text_list[int(plain_text_length/2):plain_text_length]
    left_text = plain_text_list[0:int(plain_text_length/2)]

    roundpack = [left_text, rigth_text]

    return roundpack

def encrypt(plain_text):
    roundpack = make_round_pack(plain_text)

    for i in range(0, numberKeys):
        roundpack = doRound(roundpack, i)

    roundpack = swap_keys(roundpack)
    return roundpack[0] + roundpack[1]

def decrypt(crypt_text):
    roundpack = make_round_pack(crypt_text)

    for i in reversed(range(0, numberKeys)):
        roundpack = doRound(roundpack, i)

    roundpack = swap_keys(roundpack)
    return roundpack[0] + roundpack[1]

if __name__ == "__main__":
    plain_text = 0b10010011
    key = 0b0101010101
    makeKeys(key)
    plain_text = makeLists(plain_text, plain_text_length)
    print("Plain Text: ", plain_text)

    cryp_message = encrypt(plain_text)
    plain_text = decrypt(cryp_message)

    print("Crypt: ", cryp_message)
    print("Plain: ", plain_text)
