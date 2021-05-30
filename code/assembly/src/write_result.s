#
# void write_result(int result, int valid, char * out_array)
#
# Scrive in <out_array>:
# * "Invalid" se valid = 1 oppure <result> non e' rappresentabile in 10 caratteri
# * <result> se valid = 0 e <result> e' rappresentabile in 10 caratteri
# > La funzione itoa() si occupa di convertire <result> in stringa e di scriverla in <out_array>
#
# :param int result: risultato del calcolo (o valore 'finto' in caso di valid = 1)
# :param int valid: se uguale a 0 viene scritto <result> in formato stringa, altrimenti viene scritto "Invalid"
# :param char * out_array: array/stringa su cui scrivere l'output

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

    cmpl $1, %ECX                  # se ECX != 1, <result> sembra valido
    jne write_result_valid_result  # salta all'etichetta

    # if valid == 1 (valid = False)
    xorl %EAX, %EAX                 # EAX = 0 (invalid = True)
    jmp write_result_checked_valid


write_result_valid_result:
    # Il risultato sembra valido,
    # verifico se il limite inferiore e' rispettato
    # per poter rappresentare <result> in 10 caratteri
    cmpl $-99999999, %EBX
    jge write_result_check_upper_limit

    # limite inferiore non rispettato
    xorl %EAX, %EAX                     # EAX = 0 (invalid = True)
    jmp write_result_checked_valid


write_result_check_upper_limit:
    # Il risultato sembra valido,
    # verifico se il limite superiore e' rispettato
    # per poter rappresentare <result> in 10 caratteri
    cmpl $999999999, %EBX
    jle write_result_checked_valid

    # limite superiore non rispettato
    xorl %EAX, %EAX                 # EAX = 0 (invalid = True)
    jmp write_result_checked_valid


write_result_checked_valid:
    # Ho verificato se <result> e' valido
    # oppure no valutando <valid> e i limiti
    # per rappresentare in 10 caratteri <result>
    cmpl $0, %EAX
    jne write_result_convert_result

    # if %EAX == 0 (invalid = True)
    movb $73, (%EDX)    # I
    movb $110, 1(%EDX)  # n
    movb $118, 2(%EDX)  # v
    movb $97, 3(%EDX)   # a
    movb $108, 4(%EDX)  # l
    movb $105, 5(%EDX)  # i
    movb $100, 6(%EDX)  # d
    movb $0, 7(%EDX)    # \0

    jmp write_result_fine


write_result_convert_result:
    # <result> e' valido,
    # richiamo itoa() per scriverlo
    pushl %EDX  # parametro <out_array>
    pushl %EBX  # parametro <result>
    call itoa   # itoa(result, out_array)
    popl %EBX
    popl %EDX


write_result_fine:
    popl %EDX
    popl %ECX
    popl %EBX
    popl %EAX

    popl %EBP

    ret
