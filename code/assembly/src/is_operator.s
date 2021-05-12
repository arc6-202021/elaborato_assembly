#
# int is_operator(char t_char)
#
# Questa funzione restituisce 0
# se il carattere <t_char> e' un operatore valido,
# altrimenti restituisce 1.
#
# :param char t_char: stringa con carattere in input
# :return int eax: 0 se il carattere contiene cifra, 1 altrimenti

.data

.text

    .global is_operator

is_operator:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP  # Imposta EBP alla base dello stack della funzione
    pushl %EBX       # Memorizza EBX che conterra' il parametro

    # Inizio algoritmo per la verifica dell'operatore

    movl $1, %EAX        # EAX = 1
    movl 8(%EBP), %EBX   # EBX = t_char

    # if t_char == 42: EAX = 0
    cmpb $42, %BL             # prodotto '*'
    jne is_operator_not_prod  # salta se non e' prodotto
    xorl %EAX, %EAX           # EAX = 0
    jmp is_operator_end       # so che e' prodotto, restituisci EAX

is_operator_not_prod:
    # if t_CHAR == 43: EAX = 0
    cmpb $43, %BL             # somma '+'
    jne is_operator_not_sum   # salta se non e' somma
    xorl %EAX, %EAX           # EAX = 0
    jmp is_operator_end       # so che e' somma, restituisci EAX

is_operator_not_sum:
    # if t_CHAR == 45: EAX = 0
    cmpb $45, %BL             # sottrazione '-'
    jne is_operator_not_sub   # salta se non e' sottrazione
    xorl %EAX, %EAX           # EAX = 0
    jmp is_operator_end       # so che e' sottrazione, restituisci EAX

is_operator_not_sub:
    # if t_CHAR == 47: EAX = 0
    cmpb $47, %BL             # divisione '/'
    jne is_operator_end       # salta se non e' divisione
    xorl %EAX, %EAX           # EAX = 0
                              # so che e' divisione, restituisci EAX

is_operator_end:
    # Ripristina stack e esegui return
    popl %EBX                # Reimposta EBX
    popl %EBP                # Reimposta EBP

    ret
