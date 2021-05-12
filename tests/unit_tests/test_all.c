
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

    // END OF TESTS

    if (res == 0) {
        printf("SUCCESS: all the tests returned the expected results!\n");
    }
    else {
        printf("FAIL: at least one test returned an unexpected result (%s)\n", func_name);
    }
    return res;
}
