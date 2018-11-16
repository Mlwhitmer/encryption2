from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto import Util
import argparse

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

k = 1
while 2 ** (8 * (k - 1)) <= N < 2 ** (8 * k ):
    k += 1


print(k)



