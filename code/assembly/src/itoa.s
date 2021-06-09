#
# void itoa(int num, char * output)
#
# Questa funzione converte <num> in stringa.
# La stringa viene scritta in <output>.
#
# :param int num: numero da convertire in stringa
# :param * output: stringa in output

.data

itoa_is_negative:  # flag: indica che <num> e' negativo quando vale 0
    .byte 0

.text
    .global itoa

itoa:
    # Memorizza nello stack i valori dei registri usati
    pushl %EBP
    movl %ESP, %EBP

    pushl %EAX
    pushl %EBX
    pushl %ECX
    pushl %EDX
    pushl %EDI

    # inizia algoritmo per convertire intero in stringa
    movl 8(%EBP), %EAX            # EAX = <num>
    movl 12(%EBP), %EDI           # EDI = <output>
    movb $0, itoa_is_negative     # itoa_is_negative = 0 (<num> e' negativo)
                                  # (utile quando un programma usa un ciclo:
                                  # ogni volta che la funzione viene richiamata itoa_is_negative NON viene impostato a 1 automaticamente)
    movl $0, %ECX                 # ECX = 0 (contatore numero cifre memorizzate nello stack)

    cmpl $0, %EAX                 # se EAX < 0
    jl itoa_continua_a_dividere   # salta a itoa_continua_a_dividere()

    movb $1, itoa_is_negative     # itoa_is_negative = 1 (False)
    neg %EAX                      # EAX = -EAX (cambia segno)


itoa_continua_a_dividere:
    # Richiama itoa_dividi() per dividere per 10 EAX
    # finche' EAX <= -10, poi inserisci nello stack l'ultima
    # cifra e se il numero e' negativo imposta EDI[0] = '-'

    cmpl $-10, %EAX             # se EAX <= -10
    jle itoa_dividi             # salta a itoa_dividi()

    # -- tutte le cifre meno l'ultima sono nello stack

    neg %EAX                    # cambia segno all'ultima cifra
    pushl %EAX                  # salva nello stack l'ultima cifra
    incl %ECX                   # ECX++

    xorl %EBX, %EBX             # EBX = 0 (usato per scorrere EDI)

    movb itoa_is_negative, %AL  # AL = itoa_is_negative
    cmpb $0, %AL                # se AL != 0 (<num> positivo)
    jne itoa_scrivi             # salta a itoa_scrivi()

    # numero negativo, metti meno in prima posizione
    # e sposta gli indici per scorrere EDI

    movb $45, (%EDI, %EBX)      # EDI[EBX] = '-' (EDI[0] = '-')
    incl %EBX                   # EBX++
    incl %ECX                   # ECX++
    jmp itoa_scrivi             # salta a itoa_scrivi()


itoa_dividi:
    # Ricava l'ultima cifra da EAX (EAX % 10),
    # la inserisce nello stack e impone EAX /= 10.

    movl $10, %EBX      # EBX = 10 (divisore)
    cdq                 # estendo il segno di EAX su EDX
    idivl %EBX          # EAX = EDX:EAX / EBX | EDX = EDX:EAX % EBX (EBX = 10)
    neg %EDX            # EDX = -EDX (risultato di -x/10 con x positivo e' -y)
    pushl %EDX          # memorizza cifra nello stack
    incl %ECX           # ECX++ (incrementa contatore cifre)
    jmp	itoa_continua_a_dividere


itoa_scrivi:
    # Tutte le cifre sono nello stack,
    # questa funzione recupera dallo stack le cifre,
    # le converte in carattere e le inserisce in EDI

    cmpl %ECX, %EBX         # se EBX == ECX non ho piu' cifre nello stack
    je itoa_fine            # salta a itoa_fine()

    popl %EAX               # EAX = cifra nello stack
    addb $48, %AL           # EAX += 48 (converto intero in cifra)
    movb %AL, (%EDI, %EBX)  # EDI[EBX] = EAX (aggiungo cifra alla stringa)
    incl %EBX               # incrementa di 1 l'indice

    jmp itoa_scrivi         # ritorna all'etichetta itoa_scrivi per stampare
                            # il prossimo carattere.


itoa_fine:
    # Fine algoritmo: metti \0 a fine stringa,
    # ripristina i valori dei registri e ritorna al chiamante

    movb $0, (%EDI, %ECX)  # EDI[ECX] = '\0'

    # Ripristina valori originali dei registri usati
    # e restituisci il controllo al chiamante
    popl %EDI
    popl %EDX
    popl %ECX
    popl %EBX
    popl %EAX
    popl %EBP
    ret
