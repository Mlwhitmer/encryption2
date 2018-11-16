from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto import Util
import argparse
import random

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
inp = open(key,"r")
n = inp.readline().strip()
N = inp.readline().strip()
e = inp.readline().strip()
inp.close()

#Cast read values to usable int
n = int(n)
N = int(N)
e = int(e)


#read in message
inp = open(inputFile,"r")
m = inp.readline().strip()
inp.close()

#Get r which is n/2
r = Random.get_random_bytes(int(n/2))
r = list(r)

#We must get rid of all bytes 0x00 by replacing them with a randomly chosen byte
for i in range(len(r)):
	if r[i] == 0:
		replace = Random.get_random_bytes(1)
		r[i] = int.from_bytes(replace, byteorder='big')


k = 1
while (not (2 ** (8 * (k - 1))) <= N) or (not N < 2 ** (8 * k)):
	k += 1

print(k)

b = random.randint(0, 1)
L = 8 * (k - 11) - 1
print(L)

c = []

c.append(0)
c.append(2)

#append random padding
for i in range(len(r)):
	if r[i] == 0:
		c.append(r[i])

c.append(0)
c.append(m)