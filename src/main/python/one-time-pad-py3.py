#!/usr/bin/python3
import os
import sys
import binascii

ENCODING = "utf-8"

USAGE = """
    Usage:
        $ echo "My plain text" | python one-time-pad.py -e [<rounds>]
        $ echo "pad1 pad2 ... padN ciphertext" | python one-time-pad.py -d
        $ cat cipher.txt | tr \'\\n\' \' \' | python one-time-pad.py -d
    Notes:
        - The input is always taken from stdin
        - <rounds> is an integer value that specifies how many encrypting rounds to execute
            (each encrypting round produces one additional random pad byte string)
        - The order of "pad1 pad2 ... padN ciphertext" is unimportant in the input string to be decrypted.
    """

def xorBytes(txt, key):
    return bytes([a^b for a,b in zip(txt,key)])

def doEncrypting(plain_text):
    plain_bytes = bytes(plain_text, ENCODING)
    rounds = 1
    if len(sys.argv) == 3:
        rounds = int(sys.argv[2])
    size = len(plain_bytes)
    out = [plain_bytes]
    for x in range(rounds):
        key = os.urandom(size)
        cipher_bytes = xorBytes(out[x], key)
        out[x] = key
        out.append(cipher_bytes)
    print(" ".join([x.hex().upper() for x in out]))

#import random
def doDecrypting(input_pads):
    lst = input_pads.split()
    #random.shuffle(lst) # Uncommenting and executing this line proves that the order of elements in this list is unimportant.
    lst = [binascii.unhexlify(x) for x in lst]
    out_bytes = lst[0]
    for pad_bytes in lst[1:]:
        out_bytes = xorBytes(out_bytes, pad_bytes)
    print(out_bytes.decode(ENCODING))

def main():
    #
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit()
    #
    operation = sys.argv[1]
    if operation not in ("-e", "-d", "-h", "--help"):
        sys.stderr.write("Unrecognized operation: {}\n".format(operation))
        sys.exit()
    if operation in ("-h", "--help"):
        print(USAGE)
        sys.exit()
    #
    input_txt = input() # Read input from sys.stdin
    if not input_txt:
        sys.stderr.write("No input text received.\n")
        sys.exit()
    #
    if operation == "-e":
        doEncrypting(input_txt)
    else:
        doDecrypting(input_txt)

if __name__ == "__main__":
    sys.exit(main())
