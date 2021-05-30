#
# int divisione(int a, int b)
#
# Esegue <b> / <a> e restituisce
# il risultato della divisione intera in %EAX
#
# > NOTA: il dividendo <b> deve essere positivo
#
# :param int a: primo parametro
# :param int b: secondo parametro
# :return int eax: risultato divisione intera <b> / <a>

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

    xorl %EDX, %EDX           # EDX = 0 (bit piu' significativi dividendo)
    movl 12(%EBP), %EAX       # EAX = <b> dividendo
    movl 8(%EBP), %EBX        # EBX = <a> divisore

    idiv %EBX                 # dividi EDX:EAX / EBX e metti risultato divisione in EAX
                              # (il resto ignorato va in EDX)

    # Ripristina stack e esegui return
    popl %EDX
    popl %EBX                # Reimposta EBX
    popl %EBP                # Reimposta EBP

    ret
