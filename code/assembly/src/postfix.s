.data

.text

    .global postfix

postfix:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP

    pushl %EDI
    pushl %ESI
    pushl %ECX
    pushl %EDX

    movl 8(%EBP), %ESI   # ESI = input
    movl 12(%EBP), %EDI  # EDI = output

    xorl %ECX, %ECX           # ECX = 0
    movl (%ESI, %ECX), %EDX   # EDX = ESI[0]

    movb %DL, (%EDI, %ECX)   # EDI[0] = EDX

    addl $1, %ECX          # ECX = 1
    movb $0, (%EDI, %ECX)  # EDI[1] = \0

    # Riprista registri usati e esegui return
    popl %EDX
    popl %ECX
    popl %ESI
    popl %EDI
    popl %EBP
    ret
