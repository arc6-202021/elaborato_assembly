/**
 * TEST_WRITE_RESULT
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "unittest_header.h"


int test_write_result() {
    int res;               // contiene return di sottrazione()
    int exp_res;           // contiene risultato atteso
    int success_flag = 0;  // 0 e' successo
    char output[255] = {0};
    char invalid_output[] = "Invalid\0";

    // test valori validi
    for (int result = -5000; result < 5000; result++) {

        write_result(output, 0, result);

        int length = snprintf(NULL, 0, "%d", result);  // trovo lunghezza necessaria per memorizzare k
        char* str = (char *) malloc(length + 1 );          // alloco lo spazio necessario per k e per il terminatore

        if (str != NULL) {
            snprintf(str, length + 1, "%d", result);       // converto k in stringa

            if (strcmp(output, str) != 0) {
                success_flag = 1;
                printf("result: %d, valid input returned '%s' instead\n", result, output);
            }
        }
        free(str);
    }

    // test valori esplicitamente invalidi
    for (int result = -5000; result < 5000; result++) {
        write_result(output, 1, result);
        if (strcmp(output, invalid_output) != 0) {
            success_flag = 1;
            printf("result: %d, explicit invalid returned '%s' instead\n", result, output);
        }
    }

    // basta che uno solo dei
    // risultati sia diverso da quello atteso
    // e il return sara' 1
    return success_flag;
}
