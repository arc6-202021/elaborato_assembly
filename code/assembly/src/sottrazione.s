#
# int sottrazione(int a, int b)
#
# Esegui sottrazione <b> - <a> e restituisce in %EAX il risultato.
#
# :param int a: primo parametro
# :param int b: secondo parametro
# :return int eax: risultato sottrazione <b> - <a>

.data

.text

    .global sottrazione

sottrazione:
    pushl %EBP
    movl %ESP, %EBP  # imposto esp alla base della pila

    #prendo i due parametri del metodo dalla pila ed eseguo la sottrazione
    movl 12(%EBP), %EAX # EAX = <b>
    subl 8(%EBP), %EAX  # EAX -= <a>

    popl %EBP

    ret
