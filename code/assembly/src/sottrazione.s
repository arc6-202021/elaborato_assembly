.global sottrazione

.type sottrazione, @function

sottrazione:
pushl %ebp
movl %esp,%ebp #imposto esp alla base della pila

#prendo i due parametri del metodo dalla pila ed eseguo la sottrazione
movl 8(%ebp),%eax
subl 12(%ebp),%eax

popl %ebp

ret
