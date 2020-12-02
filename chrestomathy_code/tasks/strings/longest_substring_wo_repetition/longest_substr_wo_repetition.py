import sys


def longer_substr_wo_rep_chars(s):
    max_len = 0
    char_pos = {}

    i = 0
    while i < len(s):
        if s[i] in char_pos:
            max_len = max(max_len, len(char_pos))
            i = char_pos[s[i]] + 1
            char_pos.clear()

        char_pos[s[i]] = i
        i += 1

    max_len = max(max_len, len(char_pos))
    return max_len


print(longer_substr_wo_rep_chars(sys.argv[1]))
