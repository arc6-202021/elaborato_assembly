/**
 * TEST_WRITE_RESULT
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "unittest_header.h"

#define NBIGINPUTS 8


int test_write_result() {
    int res;               // contiene return di sottrazione()
    int exp_res;           // contiene risultato atteso
    int success_flag = 0;  // 0 e' successo
    char output[255] = {0};
    char invalid_output[] = "Invalid\0";

    int big_inputs[NBIGINPUTS] = {
        2147483647,  // numero piu' grande positivo a 32 bit
        1999999999,
        1000000000,
        -100000000,
        -999999999,  // numero piu' grande negativo 9 cifre
        -1000000000,
        -1999999999,
        -2147483648, // numero piu' grande negativo a 32 bit
    };

    // test valori validi veramente
    for (int result = -2500; result < 2500; result++) {

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
    for (int result = -2500; result < 2500; result++) {
        write_result(output, 1, result);
        if (strcmp(output, invalid_output) != 0) {
            success_flag = 1;
            printf("result: %d, explicit invalid returned '%s' instead\n", result, output);
        }
    }

    // test valori apparentemente validi ma troppo grandi
    for (int i = 0; i < NBIGINPUTS; i++) {
        write_result(output, 0, big_inputs[i]);

        if (strcmp(output, invalid_output) != 0) {
            success_flag = 1;
            printf("result: %d, apparently valid but too big input returned '%s' instead\n", big_inputs[i], output);
        }
    }

    // basta che uno solo dei
    // risultati sia diverso da quello atteso
    // e il return sara' 1
    return success_flag;
}


/**
 * Quando non sara' piu' necessario il check, cancellare
 * l'altra funzione e rinominare questa togliendo "_nocheck" al nome.
*/
int test_write_result_nocheck() {
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
