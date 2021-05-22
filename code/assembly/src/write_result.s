
.data

.text

    .global write_result

write_result:
    pushl %EBP
    movl %ESP, %EBP  # imposto esp alla base della pila

    pushl %EAX
    pushl %EBX
    pushl %ECX
    pushl %EDX

    movl $1, %EAX  # EAX = invalid = 1

    # prendo i due parametri del metodo dalla pila ed eseguo il prodotto con segno
    movl 16(%EBP), %EBX   # EBX = <result>
    movl 12(%EBP), %ECX   # ECX = <valid>
    movl 8(%EBP), %EDX    # EDX = <out_array>

    cmpl $1, %ECX
    jne valid_result
    # if valid == 1
    xorl %EAX, %EAX  # EAX = 0
    jmp checked_valid

valid_result:
    cmpl $-99999999, %EBX
    jge check_upper_limit
    xorl %EAX, %EAX  # EAX = 0
    jmp checked_valid

check_upper_limit:
    cmpl $999999999, %EBX
    jle checked_valid
    xorl %EAX, %EAX  # EAX = 0
    jmp checked_valid

checked_valid:
    cmpl $0, %EAX
    jne convert_result
    # if %EAX == 0
    movb $73, (%EDX)    # I
    movb $110, 1(%EDX)  # n
    movb $118, 2(%EDX)  # v
    movb $97, 3(%EDX)   # a
    movb $108, 4(%EDX)  # l
    movb $105, 5(%EDX)  # i
    movb $100, 6(%EDX)  # d
    movb $0, 7(%EDX)    # \0

    jmp fine


convert_result:
    pushl %EDX
    pushl %EBX
    call itoa
    popl %EBX
    popl %EDX


fine:
    popl %EDX
    popl %ECX
    popl %EBX
    popl %EAX

    popl %EBP

    ret
