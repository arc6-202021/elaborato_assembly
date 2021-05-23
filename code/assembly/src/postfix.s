# Funzione principale assembly:
# scorre i caratteri dell'espressione in input,
# effettua calcoli quando trova operatori usando due elementi in cima allo stack,
# inserisce in cima allo stack gli operandi,
# e scrive in output:
# * Invalid se l'espressione in input e' invalida o se il risultato
#   della espressione non e' rappresentabile in 10 caratteri
# * altrimenti scrive il risultato dell'espressione

.data

invalid:     # input invalido. 0: True, 1: False
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

    movb $1, invalid     # invalid = 1
    xorl %EBX, %EBX      # n_stackelements = 0
    movl 8(%EBP), %ESI   # ESI = input
    movl 12(%EBP), %EDI  # EDI = output

    xorl %ECX, %ECX


postfix_loop:
    # while loop principale:
    # finche' invalid != 0 e carattere diverso
    # da \0 e \n scorri l'espressione in input

    cmpb $0,(%ESI, %ECX)  # quando legge \0 termina loop
    je postfix_fine_loop

    cmpb $10,(%ESI, %ECX) # quando legge \n termina loop
    je postfix_fine_loop

    cmpb $0, invalid      # se l'espressione in input e' invalida salta fuori dal loop
    je postfix_fine_loop

    # controlla se e' un carattere valido
    pushl (%ESI, %ECX)
    call is_valid_char
    popl %EDX            # togli dallo stack il carattere
    cmpl $0, %EAX

    # se non lo e' salta a postfix_invalid_char()
    jne postfix_invalid_char

    # carattere valido: effettuo operazioni o recupero operando
    # TODO: implementare questa parte per gestire piu' cifre e altri casi
    # https://github.com/arc6-202021/elaborato_assembly/blob/main/code/python/postfix_calculator8.py#L316-L392

    cmpb $43,(%ESI, %ECX) # quando incontra un +
    je postfix_addizione

    cmpb $45,(%ESI, %ECX) # quando incontra un -
    je postfix_sottrazione

    cmpb $42,(%ESI, %ECX) # quando incontra un *
    je postfix_prodotto

    cmpb $47,(%ESI, %ECX) # quando incontra un /
    je postfix_divisione

    cmpb $32,(%ESI, %ECX) # quando incontra uno spazio
    je postfix_spazio

    # -- ^ fine TODO L316-L392 ^
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
    inc %EBX          # n_stackelements += 1
    addl $2,%ECX      # salta un carattere (spazio) e vai al successivo
    jmp postfix_loop  # continua ciclo per leggere l'espressione


postfix_sottrazione:
    # E' stato trovato "-":
    # eseguo la sottrazione e tolgo dallo stack gli operandi

    call sottrazione
    # elimino gli ultimi due operandi dalla pila
    popl %EDX
    popl %EDX
    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    addl $2,%ECX      # salta un carattere (spazio) e vai al successivo
    jmp postfix_loop  # continua ciclo per leggere l'espressione


postfix_prodotto:
    # E' stato trovato "*":
    # calcolo il prodotto e tolgo dallo stack gli operandi

    call prodotto
    # elimino gli ultimi due operandi dalla pila
    popl %EDX
    popl %EDX
    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    addl $2,%ECX      # salta un carattere (spazio) e vai al successivo
    jmp postfix_loop  # continua ciclo per leggere l'espressione


postfix_divisione:
    # E' stato trovato "/":
    # eseguo la divisione e tolgo dallo stack gli operandi

    call divisione
    # elimino gli ultimi due operandi della pila
    popl %EDX
    popl %EDX

    pushl %EAX        # salvo il risultato
    dec %EBX          # n_stackelements -= 1 (ne ho tolti due e messo 1)
    addl $2,%ECX      # salta un carattere (spazio) e vai al successivo
    jmp postfix_loop  # continua ciclo per leggere l'espressione


postfix_spazio:
    # E' stato trovato uno spazio:
    # prendo operando della posizione precedente
    # e lo metto nella pila.

    dec %ECX               # ECX -= 1
    xorl %EDX, %EDX        # EDX = 0
    movb (%ESI,%ECX), %DL  # prelevo l'operando
    sub $48,%EDX           # converto l'operando in numero
    pushl %EDX             # metto operando nello stack
    inc %EBX               # n_stackelements += 1 (ho messo operando nello stack)
    addl $2,%ECX           # passo al prossimo carattere dopo lo spazio
    jmp postfix_loop       # continua il ciclo per leggere l'espressione


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

    # se c'e' piu' di un elemento nello stack,
    # salta a postfix_too_many_els_stack()
    cmpl $1, %EBX
    jg postfix_rm_too_many_els_stack

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
    # ci sono troppi elementi nello stack:
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
    popl %EBX
    popl %EDX
    popl %ECX
    popl %ESI
    popl %EDI
    popl %EBP
    ret
