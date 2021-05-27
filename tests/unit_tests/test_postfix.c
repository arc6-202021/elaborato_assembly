/**
 * TEST_POSTFIX
*/

#include <stdio.h>
#include <string.h>

#define NPOSTFIXTESTS 48

extern void postfix(char *, char *);

typedef struct {
    char * input;
    char * expected_output;
} postfix_test;


int main() {
    int success_flag = 0;   // 0 e' successo
    char output[255] = {0}; // contiene output di postfix()

    // casi da testare
    postfix_test test_cases[NPOSTFIXTESTS] = {
        // casi base
        {"0 0 +\0", "0\0"},
        {"0 0 -\0", "0\0"},
        {"0 0 *\0", "0\0"},
        {"0 0 +\n\0", "0\0"},
        {"0 0 -\n\0", "0\0"},
        {"0 0 *\n\0", "0\0"},

        // caratteri invalidi
        {"5 a +\0", "Invalid\0"},
        {"5 4a *\0", "Invalid\0"},

        {"4 8 3 * +\0", "28\0"},
        {"4 8 + 3 *\0", "36\0"},
        {"6 2 / 1 2 + *\0", "9\0"},
        {"8 2 / 2 2 + *\0", "16\0"},
        {"6 9 + 4 2 ^ +\0", "Invalid\0"},
        {"a 2 +\0", "Invalid\0"},
        {"-23 2 *\0", "-46\0"},

        {"     4  8     3  * +               \0", "28\0"},
        {"     4  8     3  * 23               \0", "Invalid\0"},  // 23 non e' un operatore e quindi deve dare Invalid...
        {"0 3 /\0", "0\0"},                                       // 0 / 3 = 0
        {"10 0 /\0", "Invalid\0"},


        {"\0", "Invalid\0"},
        {"                \0", "Invalid\0"},

        // operatori senza operandi
        {"-------------------\0", "Invalid\0"},

        {"  - - - -   -- - - - - - -- - - -       \0", "Invalid\0"},
        {"- - -\0", "Invalid\0"},

        // \n invece di \0
        {"4 8 3 * +\n\0", "28\0"},
        {"4 8 + 3 *\n\0", "36\0"},
        {"6 2 / 1 2 + *\n\0", "9\0"},
        {"8 2 / 2 2 + *\n\0", "16\0"},
        {"6 9 + 4 2 ^ +\n\0", "Invalid\0"},
        {"a 2 +\n\0", "Invalid\0"},
        {"-23 2 *\n\0", "-46\0"},
        {"     4  8     3  * +               \n\0", "28\0"},
        {"     4  8     3  * 23               \n\0", "Invalid\0"},  // 23 non e' un operatore e quindi deve restituire Invalid...
        {"0 3 /\n\0", "0\0"}, // # 0 / 3 = 0
        {"10 0 /\n\0", "Invalid"}, // X / 0 non si puo' calcolare
        {"\n\0", "Invalid\0"},
        {"                     \n\0", "Invalid\0"},

        // test numeri grandi
        {"999999999 0 +\0", "999999999\0"},  // 9 "9" e il terminatore: dovrebbe starci
        {"9999999999 0 +\0", "Invalid\0"},   // 10 "9": non ci sta il terminatore
        {"99999999999 0 +\0", "Invalid\0"},  // 11 "9": gia' fuori
        {"-99999999 0 +\0", "-99999999\0"},  // 8 "9", il "-" e il terminatore: dovrebbe starci
        {"-999999999 0 +\0", "Invalid\0"},   // 9 "9" e il "-": non ci sta il terminatore
        {"-9999999999 0 +\0", "Invalid\0"},  // 10 "9" e il "-"

        // test forniti dal prof
        {"30 2 + 20 -\0", "12\0"},
        {"1500 2 * 100 /\0", "30\0"},
        {"13000 -45 32 + / 1 + 1 + 1 + 2 + 3 + 5 + -800000 + 2 * 10 * 1 -\0", "-16019741\0"},
        {"13000 -45 32 + / 1 + 1 + 1 + 2 + 3 + 5 + -800000a + 2 * 10 * 1 -\0", "Invalid\0"},
        {"1 2 +@ 3 *\0", "Invalid\0"},
    };

    for (int i = 0; i < NPOSTFIXTESTS; i++) {

        postfix(test_cases[i].input, output);

        if (strcmp(output, test_cases[i].expected_output) != 0) {
            // il test fallisce
            success_flag = 1;
            printf("%s = %s (risultato atteso %s)", test_cases[i].input, output, test_cases[i].expected_output);
            printf(" RISULTATO SBAGLIATO\n");
        }
        else {
            printf("%s = %s (risultato atteso %s)\n", test_cases[i].input, output, test_cases[i].expected_output);
        }
    }

    // basta che uno solo dei
    // risultati sia diverso da quello atteso
    // e il return sara' 1
    return success_flag;
}
