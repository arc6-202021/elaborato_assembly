#
# int is_valid_char(char t_char)
#
# Questa funzione restituisce 0
# se il carattere <t_char> contiene una cifra, un operando o uno spazio
# altrimenti restituisce 1.
#
# :param char t_char: carattere in input
# :return int eax: 0 se il carattere e' valido, 1 altrimenti

.data

.text

    .global is_valid_char

is_valid_char:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP  # Imposta EBP alla base dello stack della funzione
    pushl %EBX       # Memorizza EBX che conterra' il parametro

    # Inizio algoritmo per la verifica del carattere

    movl $1, %EAX             # EAX = 1
    movl 8(%EBP), %EBX        # EBX = t_char

    # if is_operator(t_char) == 0: EAX = 0
    pushl %EBX                      # metti EBX/t_char nello stack (parametro is_operator)
    call is_operator                # richiama is_operator(EBX)
    cmpl $0, %EAX                   # controlla se il return e' zero
    jne is_valid_char_not_operator  # se e' diverso da zero, non e' operatore
    xorl %EAX, %EAX                 # se e' zero: EAX = 0
    jmp is_valid_char_end           # so che e' operatore, quindi e' valido, restituisci EAX

is_valid_char_not_operator:
    # if is_operand(t_char) == 0: EAX = 0
    call is_operand                 # nello stack c'e' ancora EBX/t_char, richiama is_operand(EBX)
    cmpl $0, %EAX                   # controlla se il return e' zero
    jne is_valid_char_not_operand   # se e' diverso da zero, non e' operando
    xorl %EAX, %EAX                 # se e' zero: EAX = 0
    jmp is_valid_char_end           # so che e' operando, quindi e' valido, restituisci EAX

is_valid_char_not_operand:
    # if t_char == 32: EAX = 0
    cmpb $32, %BL             # controlla se t_char e' spazio " "
    jne is_valid_char_end     # salta se non e' spazio
    xorl %EAX, %EAX           # se e' spazio, EAX = 0
                              # so che e' spazio, quindi e' valido, restituisci EAX

is_valid_char_end:
    # Ripristina stack e esegui return
    popl %EBX                # Rimuovo EBX/t_char dallo stack
    popl %EBX                # Reimposta EBX del chiamante
    popl %EBP                # Reimposta EBP del chiamante

    ret
