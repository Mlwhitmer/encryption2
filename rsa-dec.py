#!/usr/bin/env python3
#rsa decryption

from Crypto import Util
import argparse
import binascii


def decode(c):
        # Get the length of the byte array
        bytes_length = len(c.to_bytes((c.bit_length() + 7) // 8, 'big') or b'\0')

        plain_text_bytes = []

        padding_flag = False

        #start at 2 because we know we will the cipher texts starts with 0x00 and 0x02
        for i in range(2, bytes_length):
                if padding_flag:
                        plain_text_bytes.append(c >> (i * 8) & 0xff)
                elif (c >> (i * 8) & 0xff) == 0: #padding flag found
                        padding_flag = True

        return plain_text_bytes

def mod(m,e,n):
    if n == 1:
        return 0
    m = m % n
    r = 1
    while e > 0:
        if e % 2 == 1:
            r = (r*m) % n
        e = e >> 1
        m = m * m % n
    return r

parser = argparse.ArgumentParser()
parser.add_argument('-k','--keyfile',required = True)
parser.add_argument('-i','--inputfile',required = True)
parser.add_argument('-o','--outputfile',required = True)
args = parser.parse_args()

input = args.inputfile
key = args.keyfile
output = args.outputfile

if input is None or key is None or output is None:
        print("Incorrect usage\n")
        exit(1)

key_I = open(key,"r")

nbits = int(key_I.readline())
N = int(key_I.readline())
d = int(key_I.readline())
key_I.close()

input_I = open(input, "r")
cipher = input_I.read()

#msg = pow(int(cipher), d, N)
msg = mod(int(cipher),d,N)

#Get byte list for plain text and convert it to bytearray
plain_text_byte_array = bytearray(decode(msg))

#Convert plain_text_byte_array to a readable string
plain_text = binascii.hexlify(plain_text_byte_array).decode('utf-8')

#Open write file stream for plain text answer
out = open(output, "w")
out.write(str(plain_text))
out.close()
