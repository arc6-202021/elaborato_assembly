.data

.text

    .global postfix

postfix:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP

    movl 12(%EBP), %EBX  # EAX = output
    movl 8(%EBP), %ECX   # ECX = input

    #movl (%EBX), %ECX  # ECX = EBX[0]
    movl (%ECX), %EDX
    pushl %EDX
    call is_operator

    addl $48, %EAX
    movb %AL, (%EBX)   # EBX[0] = return is_operator
    movb $0, 1(%EBX)   # EBX[1] = \0

    #movb %CL, (%EAX)   # EAX[0] = ECX
    #movb $50, 1(%EAX)  # EAX[1] = 2
    #movb $51, 2(%EAX)  # EAX[2] = 3
    #movb $52, 3(%EAX)  # EAX[3] = 4
    #movb $0, 4(%EAX)   # EAX[4] = \0

    # Riprista registri usati e esegui return
    popl %EBP
    popl %EBP
    ret
