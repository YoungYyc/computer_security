from Crypto.Cipher import AES
import sys

with open(sys.argv[1]) as f_cipher_text:
	cipher_text = f_cipher_text.read().strip()


with open(sys.argv[2]) as f_key:
	key = f_key.read().strip()

with open(sys.argv[3]) as f_iv:
	iv = f_iv.read().strip()

cipher = AES.new(key.decode('hex'), AES.MODE_CBC, iv.decode('hex'))

msg = cipher.decrypt(cipher_text.decode('hex'))

with open(sys.argv[4], "w+") as output:
	output.write(msg.decode("ascii"))

