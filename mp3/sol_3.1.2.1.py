import sys

with open(sys.argv[1]) as f_cipher_text:
	cipher_text = f_cipher_text.read().strip()


with open(sys.argv[2]) as f_key:
	key = f_key.read().strip()

dictionary = {}
alphabet = 65 #start from A
for k in key:
	dictionary[ord(k)] = chr(alphabet) #encoded to plain text
	alphabet += 1

decipher = ""
for c in cipher_text :
	ascii = ord(c)
	if ascii <= 90 and ascii >= 65 : #is capital letter
		decipher += dictionary[ascii]
	else :
		decipher += c #keep numbers and space the same

print decipher

with open(sys.argv[3], 'w+') as output:
	output.write(decipher)

