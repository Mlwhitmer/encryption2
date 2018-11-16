#!/usr/bin/env python3
#rsa decryption

from Crypto import Util
import argparse

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

input_I = open(input,"r")
cipher = input_I.read()

msg = pow(int(cipher),d,N)

'''
output_I = open(output,"w")
output_I.write(str(m.hex()))
output_I.close()
'''
