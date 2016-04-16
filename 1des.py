"""DES implementation"""
numberKeys = 6
keys = [[0 for x in range(8)] for x in range(numberKeys)]

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

def encrypt(plaint_text):
    plain_text_list = makeLists(plain_text, 8)
    rigth_text = [None]*4
    left_text = [None]*4
    rigth_text = plain_text_list[4:8]
    left_text = plain_text_list[0:4]

def decrypt():
    pass


if __name__ == "__main__":
    plain_text = 0b00000001
    key = 0b0000000001

    makeKeys(key)
    cryp_message = encrypt(plain_text)
