/**
 * TEST_DIVISIONE
*/

#include <stdio.h>

#include "unittest_header.h"


int test_divisione() {
    int res;               // contiene return di divisione()
    int exp_res;           // contiene risultato atteso
    int success_flag = 0;  // 0 e' successo

    for (int a = 0; a < 5000; a++) {
        // divisore negativo
        for (int b = -2500; b < 0; b++) {
            res = divisione(a, b);
            exp_res = a / b;
            printf("%d / %d = %d (risultato atteso %d)", a, b, res, exp_res);
            if (exp_res != res) {
                // se la divisione non da esito atteso,
                // il test fallisce
                success_flag = 1;
                printf(" RISULTATO SBAGLIATO");
            }
            printf("\n");
        }

        // divisore positivo (no zero)
        for (int b = -2500; b > 0; b++) {
            res = divisione(a, b);
            exp_res = a / b;
            printf("%d / %d = %d (risultato atteso %d)", a, b, res, exp_res);
            if (exp_res != res) {
                // se la divisione non da esito atteso,
                // il test fallisce
                success_flag = 1;
                printf(" RISULTATO SBAGLIATO");
            }
            printf("\n");
        }
    }

    // basta che uno solo dei
    // risultati sia diverso da quello atteso
    // e il return sara' 1
    return success_flag;
}
