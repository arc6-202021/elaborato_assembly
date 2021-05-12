#
# int is_operand(char t_char)
#
# Questa funzione restituisce 0
# se il carattere <t_char> contiene una cifra,
# altrimenti restituisce 1.
#
# :param char t_char: carattere in input
# :return int eax: 0 se il carattere contiene operando valido, 1 altrimenti

.data

.text

    .global is_operand

is_operand:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP  # Imposta EBP alla base dello stack della funzione
    pushl %EBX       # Memorizza EBX che conterra' il parametro

    # Inizio algoritmo per la verifica dell'operando

    xorl %EAX, %EAX           # EAX = 0
    movl 8(%EBP), %EBX        # EBX = t_char

    # if t_char < 48: EAX = 1
    cmpb $48, %BL             # confronta codice ascii
    jge is_operand_not_below  # salta se il codice ascii e' >= 48
    movl $1, %EAX             # EAX = 1
    jmp is_operand_end        # so che non e' cifra, restituisci EAX

is_operand_not_below:
    # if t_char > 57: EAX = 1
    cmpb $57, %BL             # confronta codice ascii
    jle is_operand_end        # salta se il codice ascii e' <= 57
    movl $1, %EAX             # EAX = 1
                              # so che non e' cifra, restituisci EAX

is_operand_end:
    # Ripristina stack e esegui return
    popl %EBX                # Reimposta EBX
    popl %EBP                # Reimposta EBP

    ret
