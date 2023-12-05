#!/usr/bin/env python3

if __name__ == '__main__':
    s = input()

    flag_alphanum = False
    flag_alpha = False
    flag_num = False
    flag_lower = False
    flag_upper = False

    for letter in s:
        if (letter.isalnum()):
            flag_alphanum = True
            if (letter.isalpha()):
                flag_alpha = True
                if (letter.islower()):
                    flag_lower = True
                if (letter.isupper()):
                    flag_upper = True
            if (letter.isdigit()):
                flag_num = True

        if (flag_alphanum and flag_alpha and flag_num and flag_lower and flag_upper):
            break

    print(flag_alphanum)
    print(flag_alpha)
    print(flag_num)
    print(flag_lower)
    print(flag_upper)
