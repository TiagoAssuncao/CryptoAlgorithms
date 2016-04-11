"""DES implementation"""

keys = [][]

def makeKeys(key):
    key = key & 0b0011111111
    keylist = [(key & (1 << i)) >> i for i in reversed(range(8))]

    subkey[0:9] = key[1:10]
    subkey[10] = key[0]

def encrypt():
    pass

def decrypt():
    pass


if __name__ == "__main__":
    plain_text = 0b00000001
    key = 0b0000000001
