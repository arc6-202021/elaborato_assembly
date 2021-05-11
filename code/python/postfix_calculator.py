import sys


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


def main_c(t_input):
    """
    "Simula" il main in C: passa semplicemente la stringa a main_asm()
    e restituisce cio' che viene restituito dalla funzione.
    """ 
    asm_return = main_asm(t_input)
    return asm_return


def main_asm(t_input):
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
    invalid = False
    for element in t_input.split(" "):
        for char in element:
            if char not in ["-", "+", "*", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                invalid = True
                break
            
        if invalid:
            break

    # restituisco Invalid se sono stati trovati caratteri invalidi
    if invalid:
        result = "Invalid"
        return result

    # scorri di nuovo gli elementi
    for element in t_input.split(" "):
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

            # inserisco nello stack il risultato dell'operazione
            stack.push(op_result)
        else:
            # ho trovato operando, lo metto nello stack
            # > NOTA: e' necessaria conversione stringa -> intero
            stack.push(int(element))

    # il risultato e' l'ultimo elemento
    # > NOTA: e' necessaria conversione intero -> stringa
    result = str(stack.pop())
    return result


stack = Stack()

if __name__ == "__main__":
    
    print("Questa e' una semplice linea guida per creare l'elaborato ASM...")
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
            print(main_c(stringa))
            print("")
        
