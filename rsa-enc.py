#!/usr/bin/env python3
#rsa encryption

import os
import binascii
import math
import argparse
import random

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
e = int(key_I.readline())
key_I.close()

input_I = open(input, "r")
plain = input_I.read()
input_I.close()

num = nbits/2

arr = bytearray.fromhex(plain)

msg = [0x0, 0x2]
rng = num/8 - 3 - len(arr)

for i in range(0, int(rng)):
	rand_byte = os.urandom(1)
	byte_int = int.from_bytes(rand_byte, byteorder = 'big')
	if byte_int != 0:
		r_byte = bytearray(rand_byte)
		msg.append(r_byte[0])

msg.append(0x0)

for i in arr:
	msg.append(i)

#reverse data so it is facing the right way for decryption
msg.reverse()

m = int.from_bytes(msg, byteorder='big')

c = pow(m, e, N)

output_I = open(output, "w")

output_I.write(str(c))
output_I.close()
