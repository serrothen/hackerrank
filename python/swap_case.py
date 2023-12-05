#!/usr/bin/env python3

def swap_case(s):
    
    t = ""
    for ii in range(len(s)):
        if (s[ii].islower()):
            t += s[ii].upper()
        elif (s[ii].isupper()):
            t += s[ii].lower()
        else:
            t += s[ii]
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
