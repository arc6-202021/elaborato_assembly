.data

.text

    .global divisione

divisione:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP  # Imposta EBP alla base dello stack della funzione
    pushl %EBX       # Memorizza EBX che conterra' il parametro
    pushl %EDX

    # Inizio algoritmo per la verifica dell'operando

    xorl %EDX, %EDX           # EDX = 0
    movl 8(%EBP), %EAX        # EBX = divisore
    movl 12(%EBP), %EBX       # EAX = dividendo

    idiv %EBX

is_operand_end:
    # Ripristina stack e esegui return
    popl %EDX
    popl %EBX                # Reimposta EBX
    popl %EBP                # Reimposta EBP

    ret
