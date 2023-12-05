#!/usr/bin/env python3
import re

s = input()

m = re.match(r".*?(?P<m1>[0-9a-zA-Z])(?P=m1)",s)

if (m!=None):
    print(m.group(1))
else:
    print(-1)
