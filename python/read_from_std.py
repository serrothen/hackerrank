#!/usr/bin/env python3

import sys

content = []
for line in sys.stdin:
    content.append(line.rstrip('\n'))

a = int(content[0])
b = int(content[1])
m = int(content[2])

print( pow(a,b) )
print( pow(a,b,m) )
