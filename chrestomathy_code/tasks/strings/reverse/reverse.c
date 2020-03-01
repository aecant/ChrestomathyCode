#include <stdio.h>
#include <string.h>

void print_reversed (char *str) {
    int len = strlen(str);
    for (int i = len - 1; i >= 0; --i) {
        putchar(str[i]);
    }
}


int main (int argc, char * argv[]) {
    print_reversed(argv[1]);

    return 0;
}
