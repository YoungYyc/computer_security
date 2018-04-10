import sys
from Crypto.Hash import SHA256

with open(sys.argv[1]) as f_1:
	text_1 = f_1.read().strip() 

with open(sys.argv[2]) as f_2:
	text_2 = f_2.read().strip()

h_1 = SHA256.new()
h_1.update(text_1)

h_2 = SHA256.new()
h_2.update(text_2)

s1 = h_1.digest()
s2 = h_2.digest()

humming = sum(el1 != el2 for el1, el2 in zip(s1,s2))

with open(sys.argv[3], "w+") as output:
	output.write(hex(humming)[2:])

