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
    # guardo se gli elementi contengono caratteri non validi
    if is_valid(t_input) == 1:
        # restituisco Invalid se sono stati trovati caratteri invalidi
        result = "Invalid"
        return result

    # scorri di nuovo gli elementi
    # NOTA: sarebbe piu' efficiente fare un unico ciclo
    for element in t_input.strip("\0").split(" "):
        if element in ["-", "+", "*", "/"]:
            # ho trovato operatore, ricavo operandi dallo stack
            right_operand = stack.pop()
            left_operand = stack.pop()

            # faccio l'operazione che serve
            if element == "-":
                op_result = left_operand - right_operand
            elif element == "+":
                op_result = left_operand + right_operand
            elif element == "*":
                op_result = left_operand * right_operand
            else:
                op_result = left_operand // right_operand

            if boold:
                print("[DEBUG] Ho trovato operatore '{}': {} {} {} = {}".format(element, left_operand, element, right_operand, op_result))
            # inserisco nello stack il risultato dell'operazione
            stack.push(op_result)
        else:
            # ho trovato operando, lo metto nello stack
            # > NOTA: e' necessaria conversione stringa -> intero
            stack.push(int(element))
        
        if boold:
            stack.print()

    # il risultato e' l'ultimo elemento
    # > NOTA: e' necessaria conversione intero -> stringa
    result = str(stack.pop())
    return result


if __name__ == "__main__":
    
    # Parte utile solo per questo script Python
    # a ottenere l'input per testare l'algortimo...

    print("PROTOTIPO 2 per creare l'elaborato ASM...")
    if len(sys.argv) > 1:
        if sys.argv[1] == "dev":
            print(main_c("46 8 4 * 2 / +"))
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
