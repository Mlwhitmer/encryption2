from Crypto import Random
from Crypto import Util
import argparse
import struct
import math
import array
import binascii

def int_to_bytes(c):
	plain_text_bytes = []

	i = 0;
	loaded_byte = 999

	while loaded_byte != 0:
		loaded_byte = (c >> (i * 8) & 0xff)
		if loaded_byte != 0:
			plain_text_bytes.append(loaded_byte)
			i += 1

	plain_text_bytes.reverse()
	return plain_text_bytes

cmd = argparse.ArgumentParser()
cmd.add_argument('-k','--keyFile', required = True)
cmd.add_argument('-i','--inputFile', required = True)
cmd.add_argument('-o','--outputFile', required = True)
args = cmd.parse_args()

key = args.keyFile
inputFile = args.inputFile
outputFile = args.outputFile

if inputFile is None or key is None or outputFile is None:
	print("Incorrect usage\n")
	exit(1)


#reading in the public key information
inp = open(key, "r")
N_size = inp.readline().strip()
N = inp.readline().strip()
d = inp.readline().strip()
inp.close()

#Cast read values to usable int
N_size= int(N_size)
N = int(N)
e = int(d)


#read in message
inp = open(inputFile, "r")
m = inp.readline().strip()
inp.close()

#convert message to bytearray
m = bytearray.fromhex(m)

m_int = int.from_bytes(m, byteorder='big')

#convert message bytearray to byte list for iterating later
m = list(m)

#Get r which is n/2
r = Random.get_random_bytes(int((N_size/8)/2))
r = list(r)

#We must get rid of all bytes 0x00 by replacing them with a randomly chosen byte
for i in range(len(r)):
	if r[i] == 0:
		replace = Random.get_random_bytes(1)
		r[i] = int.from_bytes(replace, byteorder='big')

c = bytearray()

#append random padding
for i in range(len(r)):
	c.append(r[i])

#Mark the end of the random bytes
c.append(0)

#append message
for i in range(len(m)):
	c.append(m[i])

#reverse data so it is facing the right way for decryption
c.reverse()

#Convert c into something we can do math with
c = int.from_bytes(c, byteorder='big')

#Get ciphertext by encrypting
cipher_text = pow(c, e, N)

#Open write file stream for encrypted message
out = open(outputFile, "w")
out.write(str(cipher_text))
out.close()




