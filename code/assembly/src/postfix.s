.data

.text

    .global postfix

postfix:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP

    movl 12(%EBP), %EAX  # EAX = output
    movl 8(%EBP), %EBX   # EBX = input

    movl (%EBX), %ECX  # ECX = EBX[0]

    movb %CL, (%EAX)   # EAX[0] = ECX
    movb $50, 1(%EAX)  # EAX[1] = 2
    movb $51, 2(%EAX)  # EAX[2] = 3
    movb $52, 3(%EAX)  # EAX[3] = 4
    movb $0, 4(%EAX)   # EAX[4] = \0

    # Riprista registri usati e esegui return
    popl %EBP
    ret
