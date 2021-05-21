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
    e restituisce cio' che viene restituito dalla funzione.
    """
    asm_return = postfix(t_input + "\0")
    return asm_return


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


def is_valid(t_input):
    """
    Data una stringa con terminatore,
    la funzione restituisce 1 quando la stringa
    e' vuota o quando contiene caratteri non validi,
    altrimenti restituisce 0.

    I caratteri sono validi quando:
    * sono operandi
    * oppure sono operatori
    * oppure sono spazi
    > questo significa che un input di soli spazi e' considerato
    > valido ma il prof ha scritto che l'input e' ben formato (e quindi non dovrebbe essere necessario valutare questo caso)

    :param str t_input: stringa con terminatore in input
    :return int eax: 0 se la stringa contiene espressione valida, 1 altrimenti
    """
    eax = 1  # flag validita': inizialmente non valido (caso stringa di lunghezza 0)
    ecx = 0  # indice

    while t_input[ecx] != "\0":
        eax = 1  # mi preparo il flag "invalido" per il carattere

        if is_valid_char(t_input[ecx]) == 0:
            # carattere valido
            eax = 0

        # se il carattere e' invalido
        if eax == 1:
            # salta fuori dal ciclo
            break

        ecx += 1
        # salta a inizio ciclo

    # eax e' 1 per stringhe vuote o
    # almeno un carattere invalido
    return eax


def atoi(t_input, start):
    ecx = start
    eax = 0
    while t_input[ecx] != " " and t_input[ecx] != "\0" and t_input[ecx] != "\n":
        ebx = ord(t_input[ecx]) - 48
        eax = eax * 10 + ebx
        ecx += 1

    return eax


def find_stop_char(t_input, start):
    eax = start
    while t_input[eax] != " " and t_input[eax] != "\0" and t_input[eax] != "\n":
        eax += 1

    return eax


def find_next_element(t_input, start):
    eax = start
    while t_input[eax] == " ":
        if t_input[eax] == "\0" or t_input[eax] == "\n":
            break
        eax += 1

    return eax


def postfix(t_input):
    """
    Effettua il calcolo usando metodo postfix.

    Operazioni:
    * verifica se i caratteri dell'input sono validi
    * restituisce "Invalid" se non sono validi
    * se sono validi scorre di nuovo gli elementi
    * se l'elemento e' un operatore, ottiene due operandi dallo stack e calcola
    cio' che e' indicato dall'operatore e rimette il risultato nello stack
    * se l'elemento e' un operando lo mette nello stack
    * arrivati a fine input viene restituito il risultato di tutti i calcoli

    :param str t_input: stringa in input con l'espressione
    :param str result: stringa in output con il risultato
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
                    elif t_input[i] == "+":
                        # e' numero positivo, non faccio niente
                        print("piu'")
                    elif t_input[i] == "*":
                        # * e' segno invalido
                        print("per, e' invalido")
                        invalid = True
                    else:
                        # / e' segno invalido
                        print("diviso, invalido")
                        invalid = True
                elif t_input[i + 1] == " " or t_input[i + 1] == "\n" or t_input[i + 1] == "\0":
                    # i e' operatore
                    print("e' operatore...", end="")
                    if n_stackelements > 1:
                        right_operator = stack.pop()
                        left_operator = stack.pop()
                        n_stackelements -= 2

                        op_result = 0
                        if t_input[i] == "+":
                            op_result = left_operator + right_operator
                        elif t_input[i] == "-":
                            op_result = left_operator - right_operator
                        elif t_input[i] == "*":
                            op_result = left_operator * right_operator
                        else:
                            if right_operator == 0:
                                # non si puo' fare divisione per 0
                                invalid = True
                                print("non posso fare divisione per zero")
                            else:
                                op_result = left_operator // right_operator

                        if not invalid:
                            print("calcolo", left_operator, t_input[i], right_operator, "=", op_result)
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
                    if is_negative:
                        numero = - numero
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
    # > NOTA: e' necessaria conversione intero -> stringa
    if boold:
        print("")

    # solo in python occorre definire edi
    edi = ["\0", "", "", "", "", "", "", "", "", ""]
    temp_string = ["\0", "", "", "", "", "", "", "", "", ""]

    if invalid:
        # tolgo dallo stack tutto cio' che e' rimasto dai calcoli
        while n_stackelements > 0:
            random_register = stack.pop()
            n_stackelements -= 1
        edi[0] = "I"
        edi[1] = "n"
        edi[2] = "v"
        edi[3] = "a"
        edi[4] = "l"
        edi[5] = "i"
        edi[6] = "d"
        edi[7] = "\0"
    else:
        if n_stackelements == 1:
            result = stack.pop()
            ecx = 0

            # se e' minore di 0 metti segno meno e cambia segno al numero
            is_negative = False
            if result < 0:
                is_negative = True
                result = -result

            # scorri le cifre assicurandoti di non andare fuori array
            if result == 0:
                temp_string[ecx] = "0"
                ecx += 1
            else:
                while result > 0:
                    cifra = result % 10
                    if ecx < 10:
                        # chr restituisce il carattere corrispondente al codice ascii
                        temp_string[ecx] = chr(cifra + 48)
                        ecx += 1
                    else:
                        invalid = True
                    result = result // 10

            # cambia segno
            if is_negative:
                temp_string[ecx] = "-"
                ecx += 1

            # non ci sta il fine stringa: va fuori array
            if ecx > 9:
                invalid = True

            # se il risultato non sta in 10 caratteri
            if invalid:
                edi[0] = "I"
                edi[1] = "n"
                edi[2] = "v"
                edi[3] = "a"
                edi[4] = "l"
                edi[5] = "i"
                edi[6] = "d"
                edi[7] = "\0"
            else:
                # giro la stringa temporanea per avere
                # il risultato dritto
                i = 0
                ecx -= 1 # punto all'ultimo carattere della stringa temporanea
                while ecx >= 0:
                    edi[i] = temp_string[ecx]
                    ecx -= 1
                    i += 1

                edi[i] = "\0"

        else:
            # tolgo dallo stack tutto cio' che e' rimasto dai calcoli
            while n_stackelements > 0:
                random_register = stack.pop()
                n_stackelements -= 1

            edi[0] = "I"
            edi[1] = "n"
            edi[2] = "v"
            edi[3] = "a"
            edi[4] = "l"
            edi[5] = "i"
            edi[6] = "d"
            edi[7] = "\0"

    # solo in python controllo se la lunghezza dell'array e' 10 e converto l'array in stringa
    assert len(edi) == 10, "edi dovrebbe essere di 10 caratteri"
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

    print("PROTOTIPO 6 per creare l'elaborato ASM...")
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

        # testo is_valid()
        for char in string.printable:
            try:
                int(char)
                assert is_valid(char + "\0") == 0

            except ValueError:
                if char in ["-", "*", "+", "/", " "]:
                    assert is_valid(char + "\0") == 0
                else:
                    assert is_valid(char + "\0") == 1

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
            {"input": "0 3 /\n", "expected_output": "0"}, # 0 / 3 = 0
            {"input": "10 0 /\n", "expected_output": "Invalid"}, # X / 0 non si puo' calcolare
            {"input": "\n", "expected_output": "Invalid"},
            {"input": "                     \n", "expected_output": "Invalid"},

            # test forniti dal prof
            {"input": "30 2 + 20 -\0", "expected_output": "12"},
            {"input": "1500 2 * 100 /\0", "expected_output": "30"},
            {"input": "13000 -45 32 + / 1 + 1 + 1 + 2 + 3 + 5 + -800000 + 2 * 10 * 1 -\0", "expected_output": "-16019741"},
            {"input": "13000 -45 32 + / 1 + 1 + 1 + 2 + 3 + 5 + -800000a + 2 * 10 * 1 -\0", "expected_output": "Invalid"},
            {"input": "1 2 +@ 3 *\0", "expected_output": "Invalid"},
        ]
        boold = False
        for td in test_data:
            res = postfix(td["input"])
            print(td["input"], "==", res)
            assert res == td["expected_output"], "{} != {}".format(td["input"], td["expected_output"])

        print("\nSUCCESS: tutti i test hanno dato esito positivo")
    except AssertionError:
        print("\nFAIL: Uno dei test ha dato esito negativo")