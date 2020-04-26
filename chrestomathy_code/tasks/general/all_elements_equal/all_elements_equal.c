#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool all_elements_equal(int array[], int len) {
    for (int i = 1; i < len; ++i) {
        if (array[i] != array[0]) {
            return false;
        }
    }
    return true;
}

int *get_int_array(char *str_array[], int len) {
    int *int_array = malloc(len * sizeof(int));
    for (int i = 0; i < len; i++) {
        int_array[i] = atoi(str_array[i]);
    }
    return int_array;
}

int main(int argc, char *argv[]) {
    int *int_array = get_int_array(&argv[1], argc - 1);
    bool are_all_equal = all_elements_equal(int_array, argc - 1);
    printf(are_all_equal ? "_true_" : "_false_");
    free(int_array);
    return 0;
}
