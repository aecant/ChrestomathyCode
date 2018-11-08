#include <stdio.h>
#include <stdlib.h>

void print_file_content (FILE *file) {
    char c;
    while ((c = getc(file)) != EOF) {
        putchar(c);
    }
}

int main (int argc, char *argv[]) {
    if (argc > 1) {
        for (int i = 1; i < argc; ++i) {
            FILE *fin = fopen(argv[i], "r");
            if (fin == NULL) {
                printf("File %s not found\n", argv[i]);
                exit(-1);
            }
            print_file_content(fin);
            fclose(fin);
        }
    } else {
        print_file_content(stdin);
    }
    return 0;
}
