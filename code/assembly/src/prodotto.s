.global prodotto

.type prodotto, @function

prodotto:
    pushl %ebp
    movl %esp, %ebp  # imposto esp alla base della pila

    # prendo i due parametri del metodo dalla pila ed eseguo il prodotto con segno
    movl 8(%ebp), %eax
    imull 12(%ebp), %eax

    popl %ebp

    ret
