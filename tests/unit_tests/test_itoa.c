/**
 * TEST_ITOA
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "unittest_header.h"


int test_itoa() {
    int res;               // contiene return di is_valid_char()
    int success_flag = 0;  // 0 e' successo
    int i;
    char output[10] = {0};

    // scorri tutti i caratteri e testali
    for (int k = -5000; k < 5000; k++) {
        // (int) k -> (char *) str
        int length = snprintf(NULL, 0, "%d", k);  // trovo lunghezza necessaria per memorizzare k
        char* str = (char *) malloc(length + 1 );          // alloco lo spazio necessario per k e per il terminatore

        if (str != NULL) {
            snprintf(str, length + 1, "%d", k);       // converto k in stringa

            // richiamo funzione assembly itoa
            res = itoa(k, output);

            if (strcmp(output, str) != 0) {
                // se le due stringhe sono diverse,
                // qualcosa e' andato storto
                success_flag = 1;
                i = 0;
                while (output[i] != '\0') {
                    printf("%c", output[i]);
                    i++;
                }
                printf("' e' risultato inatteso per %d\n", k);
            }
        }
        else {
            printf("memoria esaurita\n");
        }
        free(str);
    }

    // basta che uno solo dei caratteri NON
    // restituisca il risultato atteso e
    // verra' restituito '1'
    return success_flag;
}
