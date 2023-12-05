#!/usr/bin/penv python3

import textwrap

def wrap(string, max_width):
    lst = textwrap.wrap(string,width=max_width)
    text = '\n'.join(lst)
    return text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
