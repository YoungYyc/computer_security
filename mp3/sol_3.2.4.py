import sys, operator, pbp
from functools import reduce
from math import floor
from fractions import gcd
from Crypto.PublicKey import RSA

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def producttree(X):
	result = [X]
	while len(X) > 1:
		X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)]
		result.append(X)
	return result

def remaindertree(ptree, T):
	result = ptree.pop()
	while ptree:
		div = ptree.pop()
		result = [result[int(floor(i/2))] % div[i]**2 for i in range(len(div))]
	rtree = [gcd(ele/n, n) for ele,n in zip(result, div)]
	return rtree

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

with open('moduli.hex', "r") as f:
    rsa_array = []
    for line in f:
        rsa_array.append(int(line,16))
    f.close()

with open('3.2.4_ciphertext.enc.asc', "r") as f:
	ciphertext = f.read()
	f.close()

ptree = producttree(rsa_array)
print 'pdone'
rtree = remaindertree(ptree, rsa_array)
print 'rdone'

pub = long('65537')
for i in range(len(rtree)):
	if rtree[i] != 1:
		p = rtree[i]
		q = rsa_array[i]/p
		priv = modinv(pub, (p-1)*(q-1))

		try:
			key = RSA.construct((p*q, pub, priv))
			plaintext = pbp.decrypt(key, ciphertext)
			print plaintext
		except ValueError:
			continue
