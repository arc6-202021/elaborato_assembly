.global addizione

.type addizione, @function

addizione:
pushl %ebp
movl %esp,%ebp #imposto esp alla base della pila

#prendo i due parametri del metodo dalla pila ed eseguo l'addizione
movl 8(%ebp),%eax
addl 12(%ebp),%eax

popl %ebp

ret
