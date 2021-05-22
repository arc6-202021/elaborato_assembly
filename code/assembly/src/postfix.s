.section .data

.text .global postfix
 
postfix:
    # Memorizza nello stack i registri usati
    pushl %EBP
    movl %ESP, %EBP

    pushl %EDI
    pushl %ESI
    pushl %ECX
    pushl %EDX

    movl 8(%EBP), %ESI   # ESI = input
    movl 12(%EBP), %EDI  # EDI = output

    xorl %ECX, %ECX

    postfix_controllo:
    cmpb $0,(%ESI, %ECX) #quando arriva alla fine e legge \0
    je postfix_fine

    cmpb $43,(%ESI, %ECX) #quando incontra un +
    je postfix_addizione

    cmpb $45,(%ESI, %ECX) #quando incontra un -
    je postfix_sottrazione

	cmpb $42,(%ESI, %ECX) #quando incontra un *
    je postfix_prodotto

	cmpb $47,(%ESI, %ECX) #quando incontra un /
    je postfix_divisione

    cmpb $32,(%ESI, %ECX) #quando incontra uno spazio
    je postfix_spazio

    jmp postfix_incrementa #quando non incontra spazio o fine

    postfix_addizione:
    call addizione
    #elimino gli ultimi due operandi della pila
    popl %EDX
    popl %EDX
    pushl %EAX #salvo il risultato
    addl $2,%ECX #scorro in avanti
    jmp postfix_controllo

    postfix_sottrazione:
    call sottrazione
    #elimino gli ultimi due operandi della pila
    popl %EDX
    popl %EDX
    pushl %EAX #salvo il risultato
    addl $2,%ECX
    jmp postfix_controllo

    postfix_prodotto:
    call prodotto
    #elimino gli ultimi due operandi della pila
    popl %EDX
    popl %EDX
    pushl %EAX #salvo il risultato
    addl $2,%ECX
    jmp postfix_controllo

    postfix_divisione:
    call divisione
    #elimino gli ultimi due operandi della pila
    popl %EDX
    popl %EDX
    pushl %EAX #salvo il risultato
    addl $2,%ECX
    jmp postfix_controllo

    #metodo che salva i vaori nella pila
    postfix_spazio:
    dec %ECX
    xorl %EDX, %EDX
    movb (%ESI,%ECX), %DL #prelevo l'operando
    sub $48,%EDX          #converto l'operando in numero
    pushl %EDX
    addl $2,%ECX #scorro al prossimo carattere
    jmp postfix_controllo

    postfix_incrementa:
    inc %ECX
    jmp postfix_controllo

    postfix_fine:
    # il risultato dell'operazione e' nello stack
    popl %EAX
    pushl %EDI #preparo i parametri che prenderà in input la funzione itoa
    pushl %EAX
    call itoa
    popl %EAX
    popl %EDI

    # Ripristina registri usati e esegui return
    popl %EDX
    popl %ECX
    popl %ESI
    popl %EDI
    popl %EBP
    ret
