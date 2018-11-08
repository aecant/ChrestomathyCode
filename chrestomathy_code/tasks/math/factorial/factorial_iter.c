#include <stdio.h>
#include <stdlib.h>

#define INV_CODE -1

unsigned long factorial (long n) {
    if (n < 0) {
        return INV_CODE;
    }
    unsigned long result = 1;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main (int argc, char *argv[]) {
    int n = atoi(argv[1]);
    unsigned long res = factorial(n);
    if (res == INV_CODE) {
        printf("_invalid_");
    } else {
        printf("%ld", res);
    }
    return 0;
}
