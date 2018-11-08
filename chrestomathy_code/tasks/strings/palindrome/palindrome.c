#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void to_lower_alpha (char *s) {
    int read, write;
    for (read = write = 0; s[read] != '\0'; ++read) {
        if (isalpha(s[read])) {
            s[write] = tolower(s[read]);
            ++write;
        }
    }
    s[write] = '\0';
}

bool is_palindrome (char *s) {
    to_lower_alpha(s);
    int last = strlen(s) - 1;
    int half = last / 2;
    for (int i = 0; i <= half; ++i) {
        if (s[i] != s[last - i]) {
            return false;
        }
    }
    return true;
}

int main (int argc, char *argv[]) {
    char *s = argv[1];
    printf(is_palindrome(s) ? "_true_" : "_false_");
    return 0;
}
