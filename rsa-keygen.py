from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto import Util
import argparse

# def inverse(a, n):
#     a = a % n
#     for x in range(1, n):
#         if ((a * x) % n == 1):
#             return x
#
#     print('modular inverse does not exist')
#     return 1

def inverse(e, Zn):

    r = Zn % e

    while not r == 1:
        Zn = e
        e = r
        r = Zn % e

    print("GOOD")
    return 1

def find_gcd(a, b):

    if a > b:
        smallest = b
    else:
        smallest = a

    for i in range(1, smallest + 1):
        if((a % i == 0) and (b % i) == 0):
            gcd = i

    return gcd

cmd = argparse.ArgumentParser()
cmd.add_argument('-p','--publicKeyFile', required = True)
cmd.add_argument('-s','--secretKeyFile', required = True)
cmd.add_argument('-n','--bitNumber', required = True)
args = cmd.parse_args()

smallPrimeList = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

publicOutput = args.publicKeyFile
privateOutput = args.secretKeyFile
n = int(args.bitNumber)

p = Util.number.getPrime(int(n/2))
q = Util.number.getPrime(int(n/2))

print("p: " + str(p))
print("q: " + str(q))

N = p * q

print("N: " + str(N))

Zn = (p-1)*(q-1)

print("Zn: " + str(Zn))

count = 0
e = smallPrimeList[count]

#find the smallest coprime to the order Zn
while not find_gcd(e, Zn) == 1:
    count += 1
    e = smallPrimeList[count]

print("e: " + str(e))

d = inverse(e, Zn)

print("d: " + str(d))

# d_calc = e % Zn
#
# print("d_calc: " + str(d_calc))

print("public key = [N: " + str(N) + " e: " + str(e) + "]")
print("private key = [N: " + str(N) + " d: " + str(d) + "]")

#Open write file stream for public key
out = open(publicOutput, "w")
out.write(str(n) + "\n")
out.write(str(N) + "\n")
out.write(str(e))
out.close()

#Open write file stream for private key
out = open(privateOutput, "w")
out.write(str(n) + "\n")
out.write(str(N) + "\n")
out.write(str(d))
out.close()



