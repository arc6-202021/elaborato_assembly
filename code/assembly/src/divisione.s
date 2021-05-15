.data

.text

    .global divisione

divisione:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP  # Imposta EBP alla base dello stack della funzione

    pushl %EBX       # Memorizza EBX che conterra' il parametro
    pushl %EDX       # Memorizza EDX per poterlo impostare a zero

    # Eseguo divisione

    xorl %EDX, %EDX           # EDX = 0 (bit piu' significativi divisore)
    movl 8(%EBP), %EAX        # EAX = dividendo
    movl 12(%EBP), %EBX       # EBX = divisore

    idiv %EBX  # dividi EDX:EAX / EBX e metti risultato divisione in EAX
               # (il resto ignorato va in EDX)

    # Ripristina stack e esegui return
    popl %EDX
    popl %EBX                # Reimposta EBX
    popl %EBP                # Reimposta EBP

    ret
