
import sys

with open(sys.argv[1]) as f_cipher_text:
	cipher = int(f_cipher_text.read().strip(),16)


with open(sys.argv[2]) as f_key:
	key = int(f_key.read().strip(),16)

with open(sys.argv[3]) as f_mod:
	N = int(f_mod.read().strip(),16)


verify = pow(cipher, key, N ) 

with open(sys.argv[4], "w+") as output:
	output.write(hex(verify)[2:-1])

