from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from Crypto import Util

# parser = argparse.ArgumentParser()
# parser.add_argument('-k','--keyfile',required = True)
# parser.add_argument('-i','--inputfile',required = True)
# parser.add_argument('-o','--outputfile',required = True)
# args = parser.parse_args()

p = Util.number.getPrime(10)
q = Util.number.getPrime(10)

print("p: " + str(p))
print("q: " + str(q))

N = p * q

print("N: " + str(N))

Zn = (p-1)*(q-1)

print("Zn: " + str(Zn))

e = 3

e


