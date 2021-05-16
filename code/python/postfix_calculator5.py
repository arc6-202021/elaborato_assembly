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
    currentelement_firstchar = -1  # memorizza l'indice del primo carattere dell'elemento che si sta leggendo
    currentelement_lastchar = -1   # memorizza l'indice dell'ultimo carattere dell'elemento che si sta leggendo
    step = 1                       # memorizza lo stato attuale del processo di lettura
    numero = 0                     # se vengono trovate cifre questa variabile contiene il numero che viene rappresentato
    moltiplicatore = 1             # moltiplicatore per le cifre (unita', decine, centinaia, migliaia, ...)
    numeric = False                # ricorda se l'attuale elemento e' numerico (operando) o no
    n_stackelements = 0            # memorizzo quanti elementi ho messo nello stack attraverso il calcolo

    while not exit and not invalid:
        if boold:
            print("sono allo step:", step)
        if step == 1:
            # cerco il primo carattere dopo spazi/inizio stringa e passo allo step 2
            # oppure ho trovato il fine stringa/nuova riga: passo allo step 5
            if t_input[i] == "\0" or t_input[i] == "\n":
                if boold:
                    print("ho trovato fine stringa")
                i -= 2 # tolgo il +1 a fine step 1 e tolgo un 1 ulteriore per tornare
                       # al carattere prima del terminatore
                step = 5

            elif t_input[i] != " ":
                currentelement_firstchar = i
                if boold:
                    print("Ho trovato il primo carattere in posizione:", currentelement_firstchar)
                step = 2

            i += 1

        elif step == 2:
            # trovo il primo spazio: il carattere prima e' l'ultimo carattere dell'elemento attuale
            if t_input[i] == " ":
                # ho trovato spazio: mi sposto una posizione prima dove ho l'ultimo carattere
                # dell'elemento, vado allo step 3
                i -= 1
                currentelement_lastchar = i
                if boold:
                    print("Ho trovato l'ultimo carattere in posizione:", currentelement_lastchar)
                step = 3
            elif t_input[i] == "\0" or t_input[i] == "\n":
                # ho trovato fine stringa: mi sposto una posizione prima dove ho l'ultimo carattere
                # dell'elemento, vado allo step 5
                i -= 1
                currentelement_lastchar = i
                if boold:
                    print("Ho trovato l'ultimo carattere della stringa in posizione:", currentelement_lastchar)
                step = 5
            else:
                # vado avanti solo se non ho trovato lo spazio
                i += 1

        elif step == 3:
            # scorro l'elemento dalla fine all'inizio
            if i < currentelement_firstchar:
                # ho finito di leggere la cifra/operatore:
                # passo allo step 4
                if numeric:
                    # se era un numero aggiungilo allo stack
                    # e resetta numero e moltiplicatore
                    if boold:
                        print("Ho finito di leggere l'operando che ha valore:", numero)
                    stack.push(numero)
                    n_stackelements += 1
                    numero = 0
                    moltiplicatore = 1
                    numeric = False
                step = 4
            else:
                if boold:
                    print("trovata cifra/operatore:", t_input[i])

                if is_operand(t_input[i]) == 0:
                    if boold:
                        print("e' operando")

                    cifra = int(t_input[i])
                    numero += cifra * moltiplicatore
                    numeric = True
                    if boold:
                        print("ora il numero da memorizzare sembra essere:", numero)
                    moltiplicatore *= 10

                elif is_operator(t_input[i]) == 0:
                    if numeric:
                        if boold:
                            print("sembra un segno...")
                        if t_input[i] == "-":
                            if boold:
                                print("e' un meno, cambio segno al numero perche' e' negativo")
                            numero = -numero
                        elif t_input[i] != "+":
                            if boold:
                                print("segno non valido: non puo' esserci / o * davanti ad un numero...")
                            invalid = True
                    else:
                        if boold:
                            print("e' operatore, faccio il calcolo e metto il risultato nello stack")

                        # verifica se ci sono abbastanza elementi nello stack
                        if n_stackelements > 1:
                            right_operand = stack.pop()
                            left_operand = stack.pop()
                            n_stackelements -= 2

                            if boold:
                                print(left_operand, t_input[i], right_operand, "=", end="")

                            if t_input[i] == "+":
                                op_result = left_operand + right_operand
                            elif t_input[i] == "-":
                                op_result = left_operand - right_operand
                            elif t_input[i] == "*":
                                op_result = left_operand * right_operand
                            else:
                                if right_operand != 0:
                                    op_result = left_operand // right_operand
                                else:
                                    # forse e' meglio trovare una alternativa migliore a mettere uno zero "a caso" nello stack...
                                    if boold:
                                        print("Si sta facendo divisione per zero! invalido")
                                    op_result = 0
                                    invalid = True

                            if boold:
                                print(op_result)
                            stack.push(op_result)
                            n_stackelements += 1
                        else:
                            # non ci sono abbastanza elementi nello stack
                            # per fare il calcolo... l'input probabilmente e' invalido
                            if boold:
                                print("ERRORE! non ci sono abbastanza elementi nello stack")
                            invalid = True
                else:
                    # non e' ne operatore ne operando (e sicuramente non e' uno spazio)...
                    # input invalido
                    if boold:
                        print("Trovato carattere invalido...")
                    invalid = True

            i -= 1

        elif step == 4:
            # torna a dove c'e' lo spazio dopo l'elemento, poi vai allo step 1
            # > se si vuole si possono spostare queste righe nello step 3
            i = currentelement_lastchar + 1
            if boold:
                print("Fine lettura elemento: sono tornato a dove c'e' lo spazio:", i)
            step = 1

        else:
            # sono allo step 5: ho trovato fine stringa
            # ho un ultimo elemento da leggere
            # oppure non ho mai trovato elementi

            if currentelement_firstchar == -1:
                if boold:
                    print("non ho mai trovato caratteri dell'espressione: e' invalida")
                invalid = True
            else:
                if boold:
                    print("ultimo elemento da leggere:")

                if i < currentelement_firstchar:
                    # ho letto l'ultimo elemento
                    if boold:
                        print("fine")
                    exit = True
                elif t_input[i] == " ":
                    # la stringa finisce con spazio/i... ho gia' il risultato nello stack
                    if boold:
                        print("la stringa finisce con spazio/i... ho gia' il risultato nello stack... fine")
                    exit = True
                else:
                    if boold:
                        print("trovata cifra/operatore dell'ultimo elemento:", t_input[i])
                    if is_operator(t_input[i]) == 0:
                        if boold:
                            print("e' operatore, faccio il calcolo e metto il risultato FINALE nello stack")

                        # controlla se ci sono abbastanza elementi nello stack prima di estrarre dati
                        if n_stackelements > 1:
                            right_operand = stack.pop()
                            left_operand = stack.pop()
                            n_stackelements -= 2

                            if boold:
                                print(left_operand, t_input[i], right_operand, "=", end="")

                            if t_input[i] == "+":
                                op_result = left_operand + right_operand
                            elif t_input[i] == "-":
                                op_result = left_operand - right_operand
                            elif t_input[i] == "*":
                                op_result = left_operand * right_operand
                            else:
                                if right_operand != 0:
                                    op_result = left_operand // right_operand
                                else:
                                    # forse e' meglio trovare una alternativa migliore a mettere uno zero "a caso" nello stack...
                                    if boold:
                                        print("Si sta facendo divisione per zero! invalido")
                                    op_result = 0
                                    invalid = True

                            if boold:
                                print(op_result)

                            stack.push(op_result)
                            n_stackelements += 1
                        else:
                            if boold:
                                print("ERRORE: non ci sono abbastanza elementi nello stack per fare l'ultimo calcolo")
                            invalid = True
                    else:
                        # non e' operatore...
                        # una espressione ben formata deve finire con un operatore
                        if boold:
                            print("Trovato carattere invalido nell'ultimo elemento...")
                        invalid = True
                i -= 1
        if boold:
            stack.print()

    # il risultato e' l'ultimo elemento
    # > NOTA: e' necessaria conversione intero -> stringa
    if boold:
        print("")

    if invalid:
        # tolgo dallo stack tutto cio' che e' rimasto dai calcoli
        for _ in range(n_stackelements):
            random_register = stack.pop()
        result = "Invalid"
    else:
        if n_stackelements == 1:
            result = str(stack.pop())
        else:
            # tolgo dallo stack tutto cio' che e' rimasto dai calcoli
            for _ in range(n_stackelements):
                random_register = stack.pop()
            result = "Invalid"

    if boold:
        stack.print()

    return result


if __name__ == "__main__":

    # Parte utile solo per questo script Python
    # a ottenere l'input per testare l'algortimo...

    print("PROTOTIPO 4 per creare l'elaborato ASM...")
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
    ]
    boold = False
    for td in test_data:
        res = postfix(td["input"])
        print(td["input"], "==", res)
        assert res == td["expected_output"], "{} != {}".format(td["input"], td["expected_output"])
