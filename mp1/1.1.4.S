.global your_asm_fn
.section .text

mp:
.string "coolfood"

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
pushl $mp
pushl $sec
pushl app

call practice
POP_CALLER_SAVE

leave
ret