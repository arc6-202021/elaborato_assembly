
#include <stdio.h>
#include <string.h>
#include "unittest_header.h"

#define FN_SIZE 255

int main() {
    int res = 0;
    int func_res = 0;
    char func_name[FN_SIZE];
    char separator[] = "========================================\n\0";

    // test_is_operator.c

    printf("Test is_operator():\n");
    func_res = test_is_operator();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_is_operator()\0");
    }

    // test_is_operand.c

    printf("Test is_operand():\n");
    func_res = test_is_operand();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_is_operand()\0");
    }

    // test_is_valid_char.c

    printf("Test is_valid_char():\n");
    func_res = test_is_valid_char();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_is_valid_char()\0");
    }

    // test_addizione.c

    printf("Test addizione():\n");
    func_res = test_addizione();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_addizione()\0");
    }

    // test_sottrazione.c

    printf("Test sottrazione():\n");
    func_res = test_sottrazione();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_sottrazione()\0");
    }

    // test_divisione.c

    printf("Test divisione():\n");
    func_res = test_divisione();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_divisione()\0");
    }

    // test_prodotto.c

    printf("Test prodotto():\n");
    func_res = test_prodotto();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_prodotto()\0");
    }

    // test_itoa.c

    printf("Test itoa():\n");
    func_res = test_itoa();
    printf("%s", separator);

    if (func_res != 0) {
        res = func_res;
        strcpy(func_name, "test_itoa()\0");
    }

    // END OF TESTS

    if (res == 0) {
        printf("SUCCESS: all the tests returned the expected results!\n");
    }
    else {
        printf("FAIL: at least one test returned an unexpected result (%s)\n", func_name);
    }
    return res;
}
