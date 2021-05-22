.section .data

is_negative:
    .byte 1

.section .text
	.global itoa

.type itoa, @function
# converte un intero in una stringa
itoa:

	pushl %EBP
    movl %ESP, %EBP

    pushl %EBX
    pushl %ECX
    pushl %EDX
	pushl %EDI
	
	movl 8(%EBP), %EAX
	movl 12(%EBP), %EDI
	movb $1, is_negative # parti dicendo che e' negativo
                         # (utile quando un programma usa un ciclo:
                         # ogni volta che la funzione viene richiamata is_negative NON viene impostato a 1 automaticamente)

    movl $0, %ecx # azzero il contatore

    cmpl $0, %EAX
    jge continua_a_dividere

    movb $0, is_negative
    neg %EAX

continua_a_dividere:

	cmp $10, %eax       # confronta 10 con il contenuto di %eax

	jge dividi			# salta all'etichetta dividi se %eax >= 10

	pushl %eax			# salva nello stack il contenuto di %eax
	inc   %ecx			# incrementa di 1 il valore di %ecx per
						# contare quante push eseguo;
						# ad ogni push salvo nello stack una cifra
						# del numero (a partire da quella meno
						# significativa)

    xorl %EBX, %EBX   # EBX = 0

    movb is_negative, %AL
    cmpb $0, %AL
    jne stampa
    movb $45, (%EDI, %EBX)
    inc %EBX
    inc %ECX

	jmp stampa			# salta all'etichetta stampa


dividi:

	movl  $0, %edx		# carica il numero 0 in %edx

	movl $10, %ebx		# carica il numero 10 in %ebx

	divl  %ebx			# divide per %ebx (10) il numero ottenuto concatenando il contenuto di %edx e %eax
 
	pushl  %edx			# salva il resto della divisione nello stack

	inc   %ecx			# incrementa il contatore delle cifre salvate nello stack

	jmp	continua_a_dividere


stampa:

	cmp   %ecx, %ebx		# controlla se ci sono ancora caratteri da stampare

	je fine_itoa		# se %ebx=0 ho stampato tutto salto alla fine della funzione

	popl  %eax			# preleva l'elemento da stampare dallo stack

	addb  $48, %al	# sommo 0 al valore in al

	movb %al,(%EDI,%EBX) # aggiungo la cifra nella stringa
    inc   %ebx			# incrementa di 1 l'indice

	jmp   stampa		# ritorna all'etichetta stampa per stampare
						# il prossimo carattere. 
fine_itoa:
    movb $0,(%EDI, %ECX)
    movl %ECX, %EAX  # restituisco la lunghezza del numero
	popl %EDI
	popl %EDX
    popl %ECX
    popl %EBX
    popl %EBP

	ret

