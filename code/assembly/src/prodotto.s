#
# int prodotto(int a, int b)
#
# Esegui prodotto tra <a> e <b> e restituisce in %EAX il risultato.
#
# :param int a: primo parametro
# :param int b: secondo parametro
# :return int eax: risultato prodotto <a> * <b>

.data

.text

    .global prodotto

prodotto:
    pushl %EBP
    movl %ESP, %EBP  # imposto esp alla base della pila

    # prendo i due parametri del metodo dalla pila ed eseguo il prodotto con segno
    movl 8(%EBP), %eax    # EAX = <a>
    imull 12(%EBP), %eax  # EAX *= <b>

    popl %EBP

    ret
