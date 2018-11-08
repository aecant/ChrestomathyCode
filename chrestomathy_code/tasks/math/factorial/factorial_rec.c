#include <stdio.h>
#include <stdlib.h>

unsigned long factorial (unsigned long n) {
    return (n < 2) ? 1 : (n * factorial(n - 1));
}

int main (int argc, char *argv[]) {
    int n = atoi(argv[1]);
    if (n < 0) {
        printf("_invalid_");
        exit(0);
    }
    printf("%ld", factorial(n));
    return 0;
}
