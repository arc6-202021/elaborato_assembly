/**
 * TEST_IS_VALID_CHAR
*/

#include <stdio.h>

#include "unittest_header.h"


int test_is_valid_char() {
    int res;               // contiene return di is_valid_char()
    int success_flag = 0;  // 0 e' successo

    // scorri tutti i caratteri e testali
    for (unsigned char k = 0; k < 255; k++) {
        res = is_valid_char(k);

        if ((k >= '0' && k <= '9') || (k == '-' || k == '+' || k == '*' || k == '/') || k == ' ') {
            // se il carattere contiene e' cifra (operando), o un operatore o uno spazio...
            if (res != 0) {
                // ...ma la funzione restituisce 1 il test fallisce
                printf("%c returned %d\n", k, res);
                success_flag = 1;
            }
        }
        else {
            // se il carattere NON e' cifra (operando), o un operatore o uno spazio ma la
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
