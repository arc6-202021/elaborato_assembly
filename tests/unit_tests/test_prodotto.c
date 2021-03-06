/**
 * TEST_PRODOTTO
*/

#include <stdio.h>

#include "unittest_header.h"


int test_prodotto() {
    int res;               // contiene return di prodotto()
    int exp_res;           // contiene risultato atteso
    int success_flag = 0;  // 0 e' successo

    for (int a = -2500; a < 2500; a++) {
        for (int b = -2500; b < 2500; b++) {
            res = prodotto(a, b);
            exp_res = a * b;

            if (exp_res != res) {
                // se la prodotto non da esito atteso,
                // il test fallisce
                success_flag = 1;
                printf("%d * %d = %d (risultato atteso %d)", a, b, res, exp_res);
                printf(" RISULTATO SBAGLIATO\n");
            }
        }
    }

    // basta che uno solo dei
    // risultati sia diverso da quello atteso
    // e il return sara' 1
    return success_flag;
}
