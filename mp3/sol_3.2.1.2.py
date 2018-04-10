from pymd5 import md5,padding
import sys
from urllib import quote 
with open(sys.argv[1]) as query_file:
	query_text = query_file.read().strip()


with open(sys.argv[2]) as command3_file:
	command3 = command3_file.read().strip()
print command3
h_known = query_text[6:6+32]
print h_known
rest = query_text[6+32+1:] 
print rest
len_text = 8 + len(rest)

padding_text = padding(len_text*8)
print padding_text
bits = (len_text + len(padding_text))*8 #bit lenth of padded text
h_ext = md5(state = h_known.decode("hex"), count = bits)

h_ext.update(command3)
print h_ext.hexdigest()

new_query = query_text[0:6] + h_ext.hexdigest() + query_text[6+32:] + quote(padding_text) + command3
print new_query

with open(sys.argv[3], "w+") as output:
	output.write(new_query)


