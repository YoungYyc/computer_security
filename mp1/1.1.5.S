.global _main

.section .data

file_name:
.ascii	"/bin/sh"

.section .text

_main:

push	%ebp
mov	%esp,%ebp

#system call
mov $11, %eax	#sys call num
mov $file_name, %ebx
mov $0, %ecx
mov $0, %edx
int $0x80    #interrupt


leave
ret