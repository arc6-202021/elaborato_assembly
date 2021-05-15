/**
 * TEST_IS_OPERATOR
*/

#include <stdio.h>

#include "unittest_header.h"


int test_is_operator() {
    int res;               // contiene return di is_operator()
    int success_flag = 0;  // 0 e' successo

    // scorri tutti i caratteri e testali
    for (unsigned char k = 0; k < 255; k++) {
        res = is_operator(k);

        if (k == '-' || k == '+' || k == '*' || k == '/') {
            // se il carattere e' un operatore ma la funzione
            // restituisce 1 il test fallisce
            if (res != 0) {
                printf("%c returned %d\n", k, res);
                success_flag = 1;
            }
        }
        else {
            // se il carattere NON e' un operatore ma la
            // funzione restituisce 0 il test fallisce
            if (res == 0) {
                printf("%c returned %d\n", k, res);
                success_flag = 1;
            }
        }
    }

    // basta che uno solo dei caratteri NON
    // restituisca il risultato atteso e
    // verra' restituito '1'
    return success_flag;
}
