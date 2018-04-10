import sys
from random import *

def update_hash(byte,outhash):
	mask = 0x3FFFFFFF
	temp = ((byte ^ 0xCC ) << 24) | ((byte ^ 0x33 ) << 16) | ((byte ^ 0xAA ) << 8) | ((byte ^ 0x55 )) 
	return (outhash & mask) + (temp & mask)

with open(sys.argv[1]) as f_1:
	text = f_1.read().strip() 
mask = 0x3FFFFFFF
outHash = 0
for b in text:
	byte = ord(b)
	outHash =  update_hash(byte,outHash)
print hex(outHash)
collision = ""
'''
pad = 0b00001100 # everytime use 10
pad_val = update_hash(pad,0)
print hex(pad_val & mask)
pad_val = update_hash(pad,pad_val)
print hex(pad_val & mask)
'''

''' 
def guess():
  count = 0
  while (1):
    print hex(count) + "/" + hex(pad_val)
    count += 1
    for guess1 in range(1,256):
      for guess2 in range(1,256):
        for guess3 in range(1,256):
          for guess4 in range(1,256):
            hash_result = update_hash(guess1,0)
            hash_result = update_hash(guess2,hash_result)
            hash_result = update_hash(guess3,hash_result)
            hash_result = update_hash(guess4,hash_result)
            print str(guess1) + " " + str(guess2)+ " " + str(guess3)+ " " + str(guess4)
            if hash_result > outHash:
              continue
            if (outHash - hash_result) % pad_val == 0 :
              return hash_result
hash_result = guess()
pad_num = (outHash - hash_result) / pad_val
pad_num *= 10


with open(sys.argv[2], "w+") as output:
	output.write(chr(guess1) + chr(guess2) + chr(guess3) + chr(guess4)+ chr(pad)*pad_num)
'''

length = len(text)
for i in range(length/2,length-1):
  collision +=  text[i]
  
for i in range(0,length/2):
  collision +=  text[i]
  
collision +=  text[length-1]
outHash = 0
for b in collision:
	byte = ord(b)
	outHash =  update_hash(byte,outHash)
print hex(outHash)

with open(sys.argv[2], "w+") as output:
	output.write(collision)
