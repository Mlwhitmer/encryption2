from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto import Util
from math import gcd as bltin_gcd

def inverse(a, n):
    a = a % n
    for x in range(1, n):
        if ((a * x) % n == 1):
            return x

    print('modular inverse does not exist')
    return 1

def coprime2(a, b):
    return bltin_gcd(a, b) == 1


# parser = argparse.ArgumentParser()
# parser.add_argument('-k','--keyfile',required = True)
# parser.add_argument('-i','--inputfile',required = True)
# parser.add_argument('-o','--outputfile',required = True)
# args = parser.parse_args()

smallPrimeList = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

p = Util.number.getPrime(10)
q = Util.number.getPrime(10)

print("p: " + str(p))
print("q: " + str(q))

N = p * q

print("N: " + str(N))

Zn = (p-1)*(q-1)

print("Zn: " + str(Zn))

count = 0
e = smallPrimeList[count]

#find the smallest coprime to the order Zn
while not coprime2(e, Zn):
    count += 1
    e = smallPrimeList[count]

print("e: " + str(e))

d = inverse(e, Zn)

print("d: " + str(d))

print("public key = [N: " + str(N) + " e: " + str(e) + "]")
print("private key = [N: " + str(N) + " d: " + str(d) + "]")


