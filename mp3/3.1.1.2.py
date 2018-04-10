
with open('3.1.1.2_value.hex') as f:
	file_content = f.read().strip()
	
integer_parsed = int(file_content,16)

print integer_parsed 

with open('sol_3.1.1.2_decimal.txt', 'w') as f_dec:
	f_dec.write(str(integer_parsed))

print bin(integer_parsed)[2:]

with open('sol_3.1.1.2_binary.txt', 'w') as f_dec:
	f_dec.write(bin(integer_parsed)[2:])

