.global your_asm_fn


.section .text

mp:
.long 0xc001f00d

sec:
.long 0xc105ed

app:
.long 0xacce55ed


.macro CALLER_SAVE
pushl %eax
pushl %ecx
pushl %edx
.endm

.macro POP_CALLER_SAVE
popl %edx
popl %ecx
popl %eax
.endm


your_asm_fn:

push	%ebp
mov	%esp,%ebp

#fix argument passed to practice
CALLER_SAVE
push mp
push sec
push app

call practice

leave
ret
