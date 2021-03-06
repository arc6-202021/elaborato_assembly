#
# void postfix(char * input, char * output)
#
# Funzione principale assembly:
# scorre i caratteri dell'espressione in input,
# effettua calcoli quando trova operatori usando due elementi in cima allo stack,
# inserisce in cima allo stack gli operandi,
# e scrive in output:
# * Invalid se l'espressione in input e' invalida o se il risultato
#   della espressione non e' rappresentabile in 10 caratteri
# * altrimenti scrive il risultato dell'espressione
#
# :param char * input: stringa input (contenuto file input + '\0')
# :param char * output: stringa output (verra' scritta nel file output dal codice C)

.data

invalid:     # input invalido. 0: True, 1: False
    .byte 1

numeric:     # flag che indica "numerico". 0: True, 1: False
    .byte 1

numero:      # variabile temporanea che memorizza operando man mano che viene letto l'input
    .long 0

is_negative: # flag che indica "numero negativo". 0: True, 1: False
    .byte 1

.text

    .global postfix

postfix:
    # Memorizza nello stack i valore originali dei registri usati
    # e imposta i valori iniziali ai registri

    pushl %EBP
    movl %ESP, %EBP

    pushl %EDI
    pushl %ESI
    pushl %ECX
    pushl %EDX
    pushl %EBX
    pushl %EAX

    movb $1, invalid     # invalid = 1
    movb $1, is_negative # is_negative = 1
    movl $0, numero      # numero = 0
    xorl %EBX, %EBX      # n_stackelements = 0
    movl 8(%EBP), %ESI   # ESI = <input>
    movl 12(%EBP), %EDI  # EDI = <output>
    xorl %ECX, %ECX      # ECX = 0 (indice per scorrere ESI)


postfix_loop:
    # while loop principale:
    # finche' invalid != 0 e carattere diverso
    # da \0 e \n scorri l'espressione in input

    cmpb $0,(%ESI, %ECX)        # quando legge \0 termina loop
    je postfix_fine_loop

    cmpb $10,(%ESI, %ECX)       # quando legge \n termina loop
    je postfix_fine_loop

    cmpb $0, invalid            # se l'espressione in input e' invalida salta fuori dal loop
    je postfix_fine_loop

    # controlla se e' un carattere valido
    pushl (%ESI, %ECX)
    call is_valid_char
    popl %EDX                   # togli dallo stack il carattere
    cmpl $0, %EAX

    jne postfix_invalid_char    # se non e' valido salta a postfix_invalid_char()

    # carattere valido: effettuo operazioni o recupero operando
    pushl (%ESI, %ECX)
    call is_operand             # controlla se ESI[ECX] e' operando
    popl %EDX                   # togli dallo stack il carattere
    cmpl $0, %EAX
    jne postfix_is_not_operand  # se ESI[ECX] non e' operando salta

    # carattere e' parte di operando
    movb $0, numeric  # numeric = 0 (ESI[ECX] e' cifra di un operando)

    # EAX = numero * 10
    pushl numero
    pushl $10
    call prodotto  # EAX = numero * 10
    popl %EDX
    popl %EDX

    xorl %EDX, %EDX         # EDX = 0
    movb (%ESI, %ECX), %DL  # EDX = ESI[ECX] (carattere letto)
    subl $48, %EDX          # converti EDX carattere in numero

    pushl %EAX  # metti nello stack numero * 10
    pushl %EDX  # metti nello stack cifra

    movb is_negative, %AL          # AL = is_negative
    cmpb $0, %AL                   # AL == 0 ?
    je postfix_number_is_negative  # salta se e' negativo

    call addizione                 # numero positivo, EAX = EAX (numero * 10) + EDX (cifra)
    jmp postfix_save_new_number    # salta per memorizzare il nuovo numero temporaneo


postfix_number_is_negative:
    # Richiama sottrazione per eseguire algoritmo:
    # EAX = EAX (numero * 10) - EDX (cifra) quando numero e' negativo
    call sottrazione


postfix_save_new_number:
    # dopo aver aggiunto la cifra al numero occorre aggiornare
    # la variabile numero
    popl %EDX
    popl %EDX

    movl %EAX, numero  # numero = EAX (numero = numero * 10 + cifra, numero positivo | - cifra se e' negativo)
    jmp postfix_incrementa_indice


postfix_is_not_operand:
    # il carattere letto non e' operando
    pushl (%ESI, %ECX)
    call is_operator
    popl %EDX            # togli dallo stack il carattere
    cmpl $0, %EAX
    jne postfix_is_not_operator

    # il carattere letto e' operatore o segno

    pushl 1(%ESI, %ECX)  # metti ESI[ECX+1] nello stack
    call is_operand      # is_operand(ESI[ECX+1])
    popl %EDX            # rimuovi operando dallo stack

    cmpl $0, %EAX
    jne postfix_next_char_is_not_operand  # se non e' operando salta

    cmpb $45,(%ESI, %ECX)      # ESI[ECX] == '-' ?
    jne postfix_segno_non_meno # salta se non e' meno

    # e' segno meno
    movb $0, is_negative          # trovato segno '-', is_negative = 0 (True)
    jmp postfix_incrementa_indice # passa al prossimo carattere


postfix_segno_non_meno:
    # non e' segno meno: puo' essere '+', '*' o '/'

    cmpb $43,(%ESI, %ECX)         # ESI[ECX] == '+' ?
    je postfix_incrementa_indice  # se e' '+' vai al prossimo carattere

    # il segno non e' un +, segno invalido
    movb $0, invalid               # ho trovato '*' o '/', segno invalido
    jmp postfix_incrementa_indice  # vai al prossimo carattere


postfix_next_char_is_not_operand:
    # il prossimo carattere non e' operando:
    # potrebbe essere un operatore

    cmpb $32, 1(%ESI, %ECX) # se prossimo carattere e' spazio
    je postfix_is_operator  # allora il carattere attuale e' operatore

    cmpb $10, 1(%ESI, %ECX) # se prossimo carattere e' \n
    je postfix_is_operator  # allora il carattere attuale e' operatore

    cmpb $0, 1(%ESI, %ECX)  # se prossimo carattere e' \0
    je postfix_is_operator  # allora il carattere attuale e' operatore

    # non e' operatore
    jmp postfix_incrementa_indice  # non e' operatore, vai al carattere successivo


postfix_is_operator:
    # ho trovato un operatore, effettuo il calcolo
    # relativo al carattere trovato

    cmpl $1, %EBX  # verifica quanti elementi sono nello stack
    jle postfix_not_enough_operands  # non ci sono abbastanza operandi nello stack per fare il calcolo

    cmpb $43,(%ESI, %ECX) # quando incontra un +
    je postfix_addizione

    cmpb $45,(%ESI, %ECX) # quando incontra un -
    je postfix_sottrazione

    cmpb $42,(%ESI, %ECX) # quando incontra un *
    je postfix_prodotto

    cmpb $47,(%ESI, %ECX) # quando incontra un /
    je postfix_divisione


postfix_not_enough_operands:
    # non ho abbastanza operandi nello stack,
    # l'input e' invalido

    movb $0, invalid  # invalid = 0 (True)
    jmp postfix_incrementa_indice


postfix_is_not_operator:
    # il carattere letto non e' operatore,
    # (e non era un operando) allora e' uno spazio

    # se non e' stato letto un operando,
    # salta a postfix_number_not_numeric()
    movb numeric, %AL
    cmpb $0, %AL
    jne postfix_number_not_numeric

    # l'elemento letto era un numero

    # inserisco numero nello stack,
    # incremento n_stackelements e
    # 'salto' a postfix_number_not_numeric()
    pushl numero  # mette operando nello stack
    inc %EBX      # incrementa n_stackelements

    # continua a postfix_number_not_numeric()


postfix_number_not_numeric:
    # resetto numeric, is_negative e numero ai valori iniziali
    # e salta a postfix_incrementa_indice()
    movb $1, numeric      # numeric = 1
    movb $1, is_negative  # is_negative = 1
    movl $0, numero       # numero = 0
    jmp postfix_incrementa_indice


postfix_invalid_char:
    # E' stato trovato carattere invalido:
    # pongo invalid = 0 e passo a postfix_incrementa_indice()
    movb $0, invalid


postfix_incrementa_indice:
    # incrementa indice per scorrere l'espressione
    # e torna a inizio loop ( postfix_loop() )
    inc %ECX
    jmp postfix_loop


postfix_addizione:
    # E' stato trovato "-":
    # eseguo la addizione e tolgo dallo stack gli operandi

    call addizione
    # elimino gli ultimi due operandi dalla pila
    popl %EDX
    popl %EDX
    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    jmp postfix_incrementa_indice


postfix_sottrazione:
    # E' stato trovato "-":
    # eseguo la sottrazione e tolgo dallo stack gli operandi

    call sottrazione
    # elimino gli ultimi due operandi dalla pila
    popl %EDX
    popl %EDX
    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    jmp postfix_incrementa_indice


postfix_prodotto:
    # E' stato trovato "*":
    # calcolo il prodotto e tolgo dallo stack gli operandi

    call prodotto
    # elimino gli ultimi due operandi dalla pila
    popl %EDX
    popl %EDX
    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    jmp postfix_incrementa_indice


postfix_divisione:
    # E' stato trovato "/":
    # eseguo la divisione e tolgo dallo stack gli operandi
    # > prima verifico se la divisione e' per zero
    popl %EDX      # EDX = operando destro
    cmpl $0, %EDX  # EDX == 0 ?
    je postfix_divide_by_zero  # se e' zero salta

    # l'operando destro non e' zero

    pushl %EDX  # rimetti l'operando destro nello stack
    call divisione
    # elimino gli ultimi due operandi della pila
    popl %EDX
    popl %EDX

    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    jmp postfix_incrementa_indice


postfix_divide_by_zero:
    # divisione per zero: metto invalid a True
    # e decremento di uno gli elementi dello stack

    dec %EBX          # n_stackelements -= 1 (lo avevo tolto per verificare se l'operando era zero)
    movb $0, invalid  # invalid = 0 (True)
    jmp postfix_incrementa_indice

# ===========================================================================================
#
#       GESTIONE SCRITTURA OUTPUT SU FILE
#       (equivalente riga 404 in poi nel prototipo: https://github.com/arc6-202021/elaborato_assembly/blob/main/code/python/postfix_calculator8.py#L404)


postfix_fine_loop:
    # Terminato il loop:
    # * Il risultato della espressione e' nello stack
    # * oppure invalid == 0 (True), l'espressione era invalida

    # se non e' invalid vai a postfix_write_appearently_valid_result(),
    cmpb $0, invalid
    jne postfix_write_appearently_valid_result

    # altrimenti continua con postfix_rm_not_used_operands_invchar()


postfix_rm_not_used_operands_invchar:
    # tolgo tutto cio' che e' stato aggiunto nello stack
    # prima di aver trovato un carattere invalido

    # se ho tolto tutto, salta a postfix_write_invalid_invchar()
    cmpl $0, %EBX
    je postfix_write_invalid_invchar

    popl %EDX  # togli elemento per elemento lo stack
    dec %EBX   # e decrementa n_stack_elements

    jmp postfix_rm_not_used_operands_invchar


postfix_write_invalid_invchar:
    # Scrivo invalid perche' sono stati
    # trovati caratteri non validi nella espressione in input

    pushl $0           # passa '<risultato>' che NON verra' scritto
    pushl $1           # passa valid = False
    pushl %EDI         # passa il puntatore array in output
    call write_result
    popl %EDI
    popl %EDX
    popl %EDX

    jmp postfix_fine   # ripristina registri e termina funzione


postfix_write_appearently_valid_result:
    # Invalid = False:
    # sempra che lo stack contenga un risultato valido
    # della espressione: cerco di scriverlo in output
    # chiamando write_result(%EDI, 0, <risultato>)

    # se non si sono elementi o c'e' piu' di un elemento nello stack,
    # salta a postfix_too_many_els_stack()
    cmpl $1, %EBX
    jne postfix_rm_too_many_els_stack

    # se c'e' un elemento nello stack, questo e' il risultato

                       # passa <risultato> della espressione (e' gia' nello stack)
    pushl $0           # passa valid = True
    pushl %EDI         # passa puntatore all'array in output
    call write_result  # scrivi <risultato>/"Invalid" in %EDI
    popl %EDI
    popl %EDX
    popl %EAX

    # e' stato scritto il valore: vado a postfix_fine()
    jmp postfix_fine


postfix_rm_too_many_els_stack:
    # ci sono troppi elementi nello stack: (oppure nessuno)
    # questo loop li rimuove e poi richiama
    # postfix_write_invalid_too_many_els_stack()

    # se (n_stackelements) EBX == 0: salta
    cmpl $0, %EBX
    je postfix_write_invalid_too_many_els_stack

    popl %EDX  # togli elemento per elemento lo stack
    dec %EBX   # e decrementa n_stack_elements

    # ripeti fino a non avere piu' elementi nello stack
    jmp postfix_rm_too_many_els_stack


postfix_write_invalid_too_many_els_stack:
    # c'erano troppi elementi nello stack:
    # sono stati rimossi e ora bisogna scrivere "Invalid"
    # nell'array in output

    pushl $0           # passa '<risultato>' che NON verra' scritto
    pushl $1           # passa valid = False
    pushl %EDI         # passa il puntatore array in output
    call write_result
    popl %EDI
    popl %EDX
    popl %EDX

    # vai a postfix_fine()


postfix_fine:
    # Ripristina registri usati e esegui return
    popl %EAX
    popl %EBX
    popl %EDX
    popl %ECX
    popl %ESI
    popl %EDI
    popl %EBP
    ret
