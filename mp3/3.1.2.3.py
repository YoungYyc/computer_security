from Crypto.Cipher import AES

def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]
    
with open("3.1.2.3_aes_weak_ciphertext.hex") as f_cipher_text:
	cipher_text = f_cipher_text.read().strip()

iv = to_bytes(0,16)

msg = ""

for key in range (0, 32) :
	cipher = AES.new(to_bytes(key,32), AES.MODE_CBC, iv)
	try: msg += (cipher.decrypt(cipher_text.decode('hex'))).decode("ascii") + " " + hex(key) + '\n'
	except UnicodeDecodeError: msg += hex(key) + '\n'

with open("3.1.2.3_out.txt", "w+") as output:
	output.write(msg)
	

