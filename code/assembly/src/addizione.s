#
# int addizione(int a, int b)
#
# Somma <a> e <b> e restituisce in %EAX il risultato.
#
# :param int a: primo parametro
# :param int b: secondo parametro
# :return int eax: risultato somma <a> + <b>

.data

.text

    .global addizione

addizione:
    pushl %ebp
    movl %esp,%ebp  # imposto esp alla base della pila

    # prendo i due parametri del metodo dalla pila ed eseguo l'addizione
    movl 8(%ebp), %eax
    addl 12(%ebp), %eax

    popl %ebp

    ret
