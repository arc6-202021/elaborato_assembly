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
    pushl %EBP
    movl %ESP, %EBP  # imposto esp alla base della pila

    # prendo i due parametri del metodo dalla pila ed eseguo l'addizione
    movl 8(%EBP), %EAX   # EAX = <a>
    addl 12(%EBP), %EAX  # EAX += <b>

    popl %EBP

    ret
