from Crypto.Cipher import AES
from Crypto import Util
import argparse
import math

PRIME_LIST = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def inverse(a, n):
    a = a % n
    for x in range(1, n):
        if ((a * x) % n == 1):
            return x

    print('modular inverse does not exist')
    return 1

def inverse(a, b):
    original_b = b
    y = 0
    x = 1

    while not a == 1:
        quotient = a // b
        t = b
        b = a % b

        a = t
        t = y

        y = x - (quotient * y)
        x = t

    if x < 0:
        x = x + original_b

    return x

def find_gcd(a, b):

    if a > b:
        smallest = b
    else:
        smallest = a

    for i in range(1, smallest + 1):
        if(a % i == 0) and (b % i) == 0:
            gcd = i

    return gcd

cmd = argparse.ArgumentParser()
cmd.add_argument('-p','--publicKeyFile', required = True)
cmd.add_argument('-s','--secretKeyFile', required = True)
cmd.add_argument('-n','--bitNumber', required = True)
args = cmd.parse_args()

publicOutput = args.publicKeyFile
privateOutput = args.secretKeyFile
n = int(args.bitNumber)

p = Util.number.getPrime(n)
q = Util.number.getPrime(n)

N = p * q

#Get the size of N in bits
N_bits = math.ceil(math.log(N, 2))

Zn = (p-1)*(q-1)
count = 0
e = PRIME_LIST[count]

#find the smallest coprime to the order Zn
while not find_gcd(e, Zn) == 1:
    count += 1
    e = PRIME_LIST[count]

d = inverse(e, Zn)

#Open write file stream for public key
out = open(publicOutput, "w")
out.write(str(N_bits) + "\n")
out.write(str(N) + "\n")
out.write(str(e))
out.close()

#Open write file stream for private key
out = open(privateOutput, "w")
out.write(str(N_bits) + "\n")
out.write(str(N) + "\n")
out.write(str(d))
out.close()



