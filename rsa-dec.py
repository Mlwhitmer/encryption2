from Crypto import Random
from Crypto import Util
import argparse
import binascii
import struct

def int_to_bytes(c):
	plain_text_bytes = []

	i = 0
	#set loaded_byte to some unubtainable value
	loaded_byte = 999

	#get bytes till 0x00 is read then stop
	while loaded_byte != 0:
		loaded_byte = (c >> (i * 8) & 0xff)
		if loaded_byte != 0:
			plain_text_bytes.append(loaded_byte)
			i += 1

	#Flip data
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

#reading in the private key information
inp = open(key, "r")
N_bits = inp.readline().strip()
N = inp.readline().strip()
d = inp.readline().strip()
inp.close()

N_bits = int(N_bits)
N = int(N)
d = int(d)

#read in message
inp = open(inputFile, "r")
cipher_text = inp.readline().strip()
inp.close()

cipher_text = int(cipher_text)

#Decipher
plaintext = pow(cipher_text, d, N)


#Get byte list for plain text and convert it to bytearray
plain_text_byte_array = bytearray(int_to_bytes(plaintext))

#Convert plain_text_byte_array to a readable string
plain_text = binascii.hexlify(plain_text_byte_array).decode('utf-8')
print(plain_text)

##Open write file stream for plain text answer
out = open(outputFile, "w")
out.write(str(plain_text))
out.close()
#




