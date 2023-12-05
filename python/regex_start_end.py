#!/usr/bin/env python3

import re

s = input()
k = input()

offset = 0
m = re.search(k,s)
if (m!=None):
    while (m!=None):
        print(f"({m.start()+offset}, {m.end()-1+offset})")
        offset += m.start()+1
        m = re.search(k,s[offset:])
else:
    print("(-1, -1)")
