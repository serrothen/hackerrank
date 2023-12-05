#!/usr/bin/env python3

import re

nline = int(input())

for ii in range(nline):
    line = input()
    lineMod = re.sub(r" &&(?= )"," and",line)
    print( re.sub(r" \|\|(?= )"," or",lineMod) )
