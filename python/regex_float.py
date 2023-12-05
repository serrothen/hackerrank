#!/usr/bin/env python3

import re

nTest = int(input())

for _ in range(nTest):
    word = input()

    valid = False
    if (re.match(r"^[+-]{0,1}[0-9]*\.[0-9]+$",word)):
        valid = True

    try:
        float(word)
    except ValueError:
        valid = False

    print(valid)
