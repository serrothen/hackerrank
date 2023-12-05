#!/usr/bin/env python3

import re

nTest = int(input())

for _ in range(nTest):
    uid = input()
    
    if (re.match(r"[a-zA-Z0-9]{10}",uid) and
        re.match(r"(.*[A-Z]){2}.*",uid) and
        re.match(r"(.*[0-9]){3}.*",uid) and
        not re.match(r".*(?P<m1>[a-zA-Z0-9]).*(?P=m1).*",uid)):
        print("Valid")
    else:
        print("Invalid")
