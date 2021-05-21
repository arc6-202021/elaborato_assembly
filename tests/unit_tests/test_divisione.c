/**
 * TEST_DIVISIONE
*/

#include <stdio.h>

#include "unittest_header.h"


int test_divisione() {
    int res;               // contiene return di divisione()
    int exp_res;           // contiene risultato atteso
    int success_flag = 0;  // 0 e' successo

    for (int b = 0; b < 5000; b++) {
        // divisore negativo
        for (int a = -2500; a < 0; a++) {
            res = divisione(a, b);
            exp_res = b / a;

            if (exp_res != res) {
                // se la divisione non da esito atteso,
                // il test fallisce
                success_flag = 1;
                printf("%d / %d = %d (risultato atteso %d)", b, a, res, exp_res);
                printf(" RISULTATO SBAGLIATO\n");
            }
        }

        // divisore positivo (no zero)
        for (int a = -2500; a > 0; b++) {
            res = divisione(a, b);
            exp_res = b / a;

            if (exp_res != res) {
                // se la divisione non da esito atteso,
                // il test fallisce
                success_flag = 1;
                printf("%d / %d = %d (risultato atteso %d)", b, a, res, exp_res);
                printf(" RISULTATO SBAGLIATO\n");
            }
        }
    }

    // basta che uno solo dei
    // risultati sia diverso da quello atteso
    // e il return sara' 1
    return success_flag;
}
