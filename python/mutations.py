#!/usr/bin/env python3

def mutate_string(string, position, character):
    #lst = list(string)
    #lst[position] = character
    #string = ''.join(lst)

    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
