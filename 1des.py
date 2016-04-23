"""DES implementation"""
import numpy
import random

numberKeys = 16
keys = [[0 for x in range(62)] for x in range(numberKeys)]
plain_text_length = 64

def create_table_permut(table_length):
    table_permut = [i for i in range(table_length)]
    create_table_permut = random.sample(table_permut, table_length)
    return create_table_permut

def permut_rever():
    rever = [None]*plain_text_length
    for i, elem in enumerate(i_permut):
        rever[elem] = i

    return rever

# Permut to plain and cripted text
i_permut = create_table_permut(plain_text_length)
rever = permut_rever()

# Permut to keys
big_key = create_table_permut(plain_text_length + 2)
small_key = create_table_permut(plain_text_length)

def permut(roundpack, table_permut):
    text = roundpack[0] + roundpack[1]
    text_permuted = [None]*table_permut.__len__()

    for i, elem in enumerate(table_permut):
        text_permuted[i] = text[elem]

    return [text_permuted[0:int((table_permut.__len__())/2)],  text_permuted[int(table_permut.__len__()/2):table_permut.__len__()]]

def swap_keys(roundpack):
    return roundpack[1], roundpack[0]

def makeLists(arg, length):
    arglist = [(arg & (1 << i)) >> i for i in reversed(range(length))]
    return arglist

def makeKeys(key):
    key = key & 0b0011111111111111111111111111111111111111111111111111111111111111
    keyList = makeLists(key, 62)
    for i in range(0, numberKeys):
        subkey = [None]*62
        subkey[0:61] = keyList[1:62]
        subkey[61] = keyList[0]
        keys[i] = subkey
        keyList = subkey

def appfuction(roundpack, current_round):
    rigth_text = roundpack[1]

    add_round_key = [0]*int(plain_text_length/2)
    current_key = keys[current_round]

    for i in range(0, rigth_text.__len__()):
        add_round_key[i] = rigth_text[i] ^ current_key[i]

    # print("saida: {0}, rigth: {1}, key: {2}.".format(add_round_key, rigth_text, current_key))
    return add_round_key

def doRound(roundpack, current_round):
    final_left_text = roundpack[1]
    left_text = roundpack[0]

    rigth_text_fuction = appfuction(roundpack, current_round)
    final_rigth_text = [0]*int(plain_text_length/2)

    for i in range(0, rigth_text_fuction.__len__()):
        final_rigth_text[i] = rigth_text_fuction[i] ^ left_text[i]

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
    roundpack = permut(roundpack, i_permut)

    for i in range(0, numberKeys):
        roundpack = doRound(roundpack, i)

    roundpack = swap_keys(roundpack)
    roundpack = permut(roundpack, rever)
    return roundpack[0] + roundpack[1]

def decrypt(crypt_text):
    roundpack = make_round_pack(crypt_text)
    roundpack = permut(roundpack, i_permut)

    for i in reversed(range(0, numberKeys)):
        roundpack = doRound(roundpack, i)

    roundpack = swap_keys(roundpack)
    roundpack = permut(roundpack, rever)
    return roundpack[0] + roundpack[1]

if __name__ == "__main__":
    plain_text = 0b1111111100100110010011001001100100110010011001001100100110010011
    key = 0b1101101011111100110110101110110101110110101110110101110110101001

    makeKeys(key)
    plain_text = makeLists(plain_text, plain_text_length)
    temp = plain_text
    cryp_message = encrypt(plain_text)
    plain_text = decrypt(cryp_message)

    assert(temp == plain_text)
