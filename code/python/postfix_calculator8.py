import sys

boold = True

# =============== MEMORIA - STACK ===============


class Stack():
    def __init__(self):
        """
        Simula lo stack.

        __memory simula celle di memoria
        """
        self.__memory = []

    def push(self, data):
        """
        Inserisce <data> nello stack.

        :param data: dato da inserire nello stack
        """
        self.__memory.append(data)

    def pop(self):
        """
        Rimuove e restituisce l'ultimo elemento inserito nello stack.
        :return removed: elemento rimosso dallo stack
        """
        removed = self.__memory.pop()
        return removed

    def print(self):
        """
        Visualizza la memoria sotto forma di lista.
        """
        print("[DEBUG] STACK: ", self.__memory.__repr__())


# creo stack globale
stack = Stack()

# =============== MAIN C ===============


def main_c(t_input):
    """
    "Simula" il main in C: passa semplicemente la stringa a postfix()
    concatenando alla fine il carattere di fine stringa
    e edi, array in cui viene restituito il risultato.

    Solo in python main_c() restuisce al chiamante la lista ottenuta.

    :param str t_input: stringa in input con espressione senza terminatore (simula la lettura file del main.c)
    :return list edi: lista con output (invalid o risultato espressione)
    """
    edi = ["\0", "", "", "", "", "", "", "", "", "", "", ""]
    postfix(t_input + "\0", edi)
    return edi


# =============== ASSEMBLY ===============


def is_operator(t_char):
    """
    Questa funzione restituisce 0
    se il carattere <t_char> e' un operatore valido,
    altrimenti restituisce 1.

    :param str t_char: stringa con carattere in input
    :return int eax: 0 se il carattere contiene cifra, 1 altrimenti
    """
    eax = 1
    if ord(t_char) == 42:
        # prodotto *
        eax = 0

    if ord(t_char) == 43:
        # somma +
        eax = 0

    if ord(t_char) == 45:
        # sottrazione -
        eax = 0

    if ord(t_char) == 47:
        # divisione /
        eax = 0

    return eax


def is_operand(t_char):
    """
    Questa funzione restituisce 0
    se il carattere <t_char> contiene una cifra,
    altrimenti restituisce 1.
    :param str t_char: stringa con carattere in input
    :return int eax: 0 se il carattere contiene operando valido, 1 altrimenti
    """
    eax = 0 # parto dicendo che e' un numero

    if ord(t_char) < 48:
        # non e' numero (ascii < carattere "0")
        eax = 1

    if ord(t_char) > 57:
        # non e' numero (ascii > carattere "9")
        eax = 1

    return eax


def is_valid_char(t_char):
    """
    La funzione restituisce 1 quando il carattere
    e' non valido,
    altrimenti restituisce 0.

    Il carattere e' valido quando:
    * e' operandi
    * oppure e' operatori
    * oppure e' uno spazio

    :param str t_char: carattere in input
    :return int eax: 0 se il carattere e' valido, 1 altrimenti
    """
    eax = 1  # mi preparo il flag "invalido" per il carattere

    # se il carattere e' un operatore, un operando o uno spazio
    # il carattere e' valido
    if is_operator(t_char) == 0:
        # e' operatore
        eax = 0

    if is_operand(t_char) == 0:
        # e' operando
        eax = 0

    if ord(t_char) == 32:
        # e' uno spazio
        eax = 0

    return eax


def addizione(a, b):
    """
    Somma a + b e restituisce il risultato in eax.
    > NOTA: in assembly non e' esattamente cosi'

    :param int a: primo parametro
    :param int b: secondo parametro
    :return in eax: risultato operazione
    """
    eax = a + b
    if boold:
        print(a, "+", b, "=", eax)
    return eax


def divisione(a, b):
    """
    Fa divisione intera a / b e restituisce il risultato in eax.
    > NOTA: in assembly non e' esattamente cosi'

    :param int a: primo parametro
    :param int b: secondo parametro
    :return in eax: risultato operazione
    """
    eax = a // b
    if boold:
        print(a, "/", b, "=", eax)
    return eax


def prodotto(a, b):
    """
    Esegue prodotto a * b e restituisce il risultato in eax.
    > NOTA: in assembly non e' esattamente cosi'

    :param int a: primo parametro
    :param int b: secondo parametro
    :return in eax: risultato operazione
    """
    eax = a * b
    if boold:
        print(a, "*", b, "=", eax)
    return eax


def sottrazione(a, b):
    """
    Esegue sottrazione a - b e restituisce il risultato in eax.
    > NOTA: in assembly non e' esattamente cosi'

    :param int a: primo parametro
    :param int b: secondo parametro
    :return in eax: risultato operazione
    """
    eax = a - b
    if boold:
        print(a, "-", b, "=", eax)
    return eax


def itoa(num, out_array):
    """
    Converte num in stringa (array di caratteri).
    > NOTA: guardare il file code/assembly/itoa.s per l'algoritmo assembly

    :param int num: numero da convertire
    :param list out_array: array di caratteri (output della funzione, puntatore in assembly)
    """
    i = 0
    for char in str(num):
        out_array[i] = char
        i += 1

    out_array[i] = "\0"


def write_result(edi, valid, result):
    """
    La funzione scrive <result> nell'array in output <edi>
    se <result> puo' stare in 10 caratteri.
    > se e' negativo puo' avere fino 8 cifre piu' il segno, se e' positivo 9 cifre.
    > Il decimo carattere serve per il terminatore

    Se <result> non sta nei 10 caratteri oppure valid == 1
    in <edi> verra' scritto "Invalid".

    :param list edi: lista su cui scrivere l'output (puntatore in assembly)
    :param int valid: se 0 l'output sembra valido (occorre verificare la lunghezza), altrimenti non valido
    :param int result: risultato della espressione data in input al programma
    """

    invalid = 1
    if valid == 1:
        # non e' valido
        invalid = 0

    if invalid == 0:
        edi[0] = "I"
        edi[1] = "n"
        edi[2] = "v"
        edi[3] = "a"
        edi[4] = "l"
        edi[5] = "i"
        edi[6] = "d"
        edi[7] = "\0"
    else:
        itoa(result, edi)


def postfix(t_input, edi):
    """
    Effettua il calcolo usando metodo postfix.

    Operazioni:
    * scorre l'input verificando carattere per carattere dell'input se sono validi
    * restituisce in <edi> "Invalid" se almeno un carattere non e' valido
        > "Invalid" viene inserito in <edi> grazie a write_result()

    * se sono validi verifica se e' operatore, operando o spazio
    * se l'elemento e' un operatore, ottiene due operandi dallo stack e calcola
    cio' che e' indicato dall'operatore e rimette il risultato nello stack
    * se l'elemento e' un operando memorizza ogni cifra trovata in numero e al primo spazio lo mette nello stack
    * (se e' uno spazio mette il numero letto, se e' stato letto, nello stack)
    * arrivati a fine input viene restituito il risultato di tutti i calcoli in <edi>
        > il valore viene scritto da write_result()

    Tutto viene fatto memorizzando quanti elementi vengono inseriti e tolti dallo stack
    per ripristinare sempre lo stack alla situazione iniziale e fare un return sicuro
    > se alla fine del calcolo c'e' piu' di un elemento il risultato sara' "Invalid"

    :param str t_input: stringa in input con l'espressione
    :param list edi: stringa (array di caratteri) in output con il risultato
    """
    # scorri gli elementi
    # nella stringa controllando se sono validi

    if boold:
        for el in t_input:
            print(el + "\t|", end="")
        print("")
        for i in range(len(t_input)):
            print(str(i) + "\t|", end="")
        print("")

    i = 0                          # indice per scorrere
    invalid = False                # quando va a True l'input e' invalido e il loop termina
    exit = False                   # quando va a True ho letto tutto l'input e il loop termina
    numero = 0                     # se vengono trovate cifre questa variabile contiene il numero che viene rappresentato
    numeric = False                # ricorda se l'attuale elemento e' numerico (operando) o no
    n_stackelements = 0            # memorizzo quanti elementi ho messo nello stack attraverso il calcolo
    is_negative = False            # se ho trovato segno meno davanti al numero devo cambiare il segno a fine lettura

    while not exit and not invalid:
        print(t_input[i])
        if t_input[i] == "\0":
            print("sono alla fine perche' ho trovato \\0")
            exit = True
        elif t_input[i] == "\n":
            print("sono alla fine perche' ho trovato \\n")
            exit = True
        elif is_valid_char(t_input[i]) == 0:
            print("letto carattere valido... ", end="")
            if is_operand(t_input[i]) == 0:
                print("e' un numero...")
                # sto leggendo numero positivo
                numeric = True
                cifra = ord(t_input[i]) - 48
                if is_negative:
                    numero = numero * 10 - cifra
                else:
                    numero = numero * 10 + cifra
                print("numero letto fino ad ora:", numero)
            elif is_operator(t_input[i]) == 0:
                # sto leggendo operatore o segno
                print("e' operatore o segno... ", end="")
                if is_operand(t_input[i + 1]) == 0:
                    # i e' segno
                    print("e' segno... ", end="")
                    if t_input[i] == "-":
                        # e' numero negativo, ricordo di cambiare segno quando trovo spazio
                        is_negative = True
                        print("meno")
                    elif t_input[i] == "*":
                        # * e' segno invalido
                        print("per, e' invalido")
                        invalid = True
                    else:
                        # / e' segno invalido
                        print("diviso, invalido")
                        invalid = True

                    # se e' + e' numero positivo, non faccio niente
                    # > NOTA: non serve convertire questo if in assembly
                    if t_input[i] == "+":
                        print("piu', lo ignoro")

                elif t_input[i + 1] == " " or t_input[i + 1] == "\n" or t_input[i + 1] == "\0":
                    # i e' operatore
                    print("e' operatore...", end="")
                    if n_stackelements > 1:
                        right_operator = stack.pop()
                        left_operator = stack.pop()
                        n_stackelements -= 2

                        op_result = 0
                        if t_input[i] == "+":
                            op_result = addizione(left_operator, right_operator)
                        elif t_input[i] == "-":
                            op_result = sottrazione(left_operator, right_operator)
                        elif t_input[i] == "*":
                            op_result = prodotto(left_operator, right_operator)
                        else:
                            if right_operator == 0:
                                # non si puo' fare divisione per 0
                                invalid = True
                                print("non posso fare divisione per zero")
                            else:
                                op_result = divisione(left_operator, right_operator)

                        if not invalid:
                            stack.push(op_result)
                            n_stackelements += 1
                    else:
                        # non ci sono abbastanza elementi nello stack
                        print("non ci sono abbastanza operandi nello stack")
                        invalid = True

            else:
                # sto leggendo spazio
                print("ho letto spazio...", end="")
                # se avevo trovato numero lo metto nello stack
                if numeric:
                    print("ho terminato di leggere un numero", end="")
                    stack.push(numero)
                    n_stackelements += 1
                print("")
                numeric = False
                is_negative = False
                numero = 0
        else:
            print("carattere invalido")
            invalid = True

        stack.print()
        i += 1

    # il risultato e' l'ultimo elemento
    if boold:
        print("")

    # -- scrivo il risultato se valido, altrimenti scrivo "Invalid"

    if invalid:
        # tolgo dallo stack tutto cio' che e' rimasto dai calcoli
        while n_stackelements > 0:
            random_register = stack.pop()
            n_stackelements -= 1
        write_result(edi, 1, 0)  # scrivi invalid
    else:
        if n_stackelements == 1:
            result = stack.pop()
            # se il risultato non e' troppo lungo scrivilo in edi
            write_result(edi, 0, result)
        else:
            # tolgo dallo stack tutto cio' che e' rimasto dai calcoli
            while n_stackelements > 0:
                random_register = stack.pop()
                n_stackelements -= 1

            write_result(edi, 1, 0)  # scrivi invalid

    # solo in python controllo se la lunghezza dell'array e' 12 e converto l'array in stringa
    assert len(edi) == 12, "edi dovrebbe essere di 12 caratteri"
    print(edi)
    result = "".join(edi).split("\0")[0]
    print("risultato finale: ", result)
    print("lo stack dovrebbe essere vuoto: ", end="")
    stack.print()

    # sempre solo per python: controllo che lo stack sia vuoto
    try:
        a = stack.pop()
        raise Exception("lo stack NON e' vuoto!")
    except IndexError:
        # non riesco a togliere niente dallo stack
        # perche' la lista e' vuota: successo
        pass

    return result


if __name__ == "__main__":

    # Parte utile solo per questo script Python
    # a ottenere l'input per testare l'algortimo...

    print("PROTOTIPO 7 per creare l'elaborato ASM...")
    if len(sys.argv) > 1:
        if sys.argv[1] == "dev":
            print(main_c("46 8 -4 * 2 / +"))
        else:
            print(main_c(sys.argv[1]))
    else:
        stringa = ""
        while stringa.strip() != "exit":
            print("Scrivi 'exit' per uscire")
            stringa = input("Inserisci l'input: ")
            if stringa.strip() != "exit":
                print(main_c(stringa))
                print("")

    print("=" * 50)
    print("AREA TEST")

    # -- AREA DEI TEST: SARANNO DA SCRIVERE IN C

    import string

    try:
        # mi assicuro che is_operator() restituisce 0 solo per gli operatori validi
        for char in string.printable:
            if char in ["-", "*", "+", "/"]:
                assert is_operator(char) == 0
            else:
                assert is_operator(char) == 1

        # se il carattere e' convertibile in numero, quella e' una cifra dell'operando
        for char in string.printable:
            try:
                int(char)
                assert is_operand(char) == 0

            except ValueError:
                assert is_operand(char) == 1

        # testo is_valid_char()
        for char in string.printable:
            try:
                int(char)
                assert is_valid_char(char) == 0

            except ValueError:
                if char in ["-", "*", "+", "/", " "]:
                    assert is_valid_char(char) == 0
                else:
                    assert is_valid_char(char) == 1

        # testo postfix()
        test_data = [
            {"input": "4 8 3 * +\0", "expected_output": "28"},
            {"input": "4 8 + 3 *\0", "expected_output": "36"},
            {"input": "6 2 / 1 2 + *\0", "expected_output": "9"},
            {"input": "8 2 / 2 2 + *\0", "expected_output": "16"},
            {"input": "6 9 + 4 2 ^ +\0", "expected_output": "Invalid"},
            {"input": "a 2 +\0", "expected_output": "Invalid"},
            {"input": "-23 2 *\0", "expected_output": "-46"},

            {"input": "     4  8     3  * +               \0", "expected_output": "28"},
            {"input": "     4  8     3  * 23               \0", "expected_output": "Invalid"},  # 23 non e' un operatore...
            {"input": "0 0 +\0", "expected_output": "0"},
            {"input": "0 3 /\0", "expected_output": "0"}, # 0 / 3 = 0
            {"input": "10 0 /\0", "expected_output": "Invalid"}, # X / 0 non si puo' calcolare
            {"input": "\0", "expected_output": "Invalid"},
            {"input": "                \0", "expected_output": "Invalid"},

            # operatori senza operandi
            {"input": "-------------------\0", "expected_output": "Invalid"},
            {"input": "  - - - -   -- - - - - - -- - - -       \0", "expected_output": "Invalid"},
            {"input": "- - -\0", "expected_output": "Invalid"},

            # \n invece di \0
            {"input": "4 8 3 * +\n", "expected_output": "28"},
            {"input": "4 8 + 3 *\n", "expected_output": "36"},
            {"input": "6 2 / 1 2 + *\n", "expected_output": "9"},
            {"input": "8 2 / 2 2 + *\n", "expected_output": "16"},
            {"input": "6 9 + 4 2 ^ +\n", "expected_output": "Invalid"},
            {"input": "a 2 +\n", "expected_output": "Invalid"},
            {"input": "-23 2 *\n", "expected_output": "-46"},
            {"input": "     4  8     3  * +               \n", "expected_output": "28"},
            {"input": "     4  8     3  * 23               \n", "expected_output": "Invalid"},  # 23 non e' un operatore...
            {"input": "0 0 +\n", "expected_output": "0"},
            {"input": "0 0 -\n", "expected_output": "0"},
            {"input": "0 0 *\n", "expected_output": "0"},
            {"input": "0 3 /\n", "expected_output": "0"}, # 0 / 3 = 0
            {"input": "10 0 /\n", "expected_output": "Invalid"}, # X / 0 non si puo' calcolare
            {"input": "\n", "expected_output": "Invalid"},
            {"input": "                     \n", "expected_output": "Invalid"},

            # test numeri grandi
            {"input": "999999999 0 +\0", "expected_output": "999999999"},      # 9 "9" e il terminatore: 10 caratteri in tutto
            {"input": "2147483647 0 +\0", "expected_output": "2147483647"},    # numero piu' grande rappresentabile in 32 bit
            {"input": "-99999999 0 +\0", "expected_output": "-99999999"},      # 8 "9", il "-" e il terminatore: 10 caratteri
            {"input": "-999999999 0 +\0", "expected_output": "-999999999"},    # 9 "9" e il "-" e il terminatore: 11 caratteri
            {"input": "-2147483648 0 +\0", "expected_output": "-2147483648"},  # numero piu' piccolo rappresentabile in 32 bit

            # test forniti dal prof
            {"input": "30 2 + 20 -\0", "expected_output": "12"},
            {"input": "1500 2 * 100 /\0", "expected_output": "30"},
            {"input": "13000 -45 32 + / 1 + 1 + 1 + 2 + 3 + 5 + -800000 + 2 * 10 * 1 -\0", "expected_output": "-16019741"},
            {"input": "13000 -45 32 + / 1 + 1 + 1 + 2 + 3 + 5 + -800000a + 2 * 10 * 1 -\0", "expected_output": "Invalid"},
            {"input": "1 2 +@ 3 *\0", "expected_output": "Invalid"},
        ]
        boold = False
        for td in test_data:
            edi = ["\0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            print("TEST INPUT:", td["input"])
            postfix(td["input"], edi)
            res = "".join(edi).split("\0")[0]
            print(td["input"], "=", "'" + res + "'")
            assert res == td["expected_output"], "{} != {}".format(td["input"], td["expected_output"])
            print("-" * 50)

        print("\nSUCCESS: tutti i test hanno dato esito positivo")
    except AssertionError as e:
        print("\nTest fallito:", e)
        print("\nFAIL: Uno dei test ha dato esito negativo")
