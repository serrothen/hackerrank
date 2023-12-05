#!/usr/bin/env python3

import re

nAddresses = int(input())

for _ in range(nAddresses):
    name,dummy = list(input().split())
    mail = dummy.removeprefix("<").removesuffix(">")

    valid = False
    if (mail!=""):
        if (re.match(r"[a-zA-Z]",mail[0]) and
            re.match(r"[a-zA-Z0-9-._]*@[a-zA-Z]*\.[a-zA-Z]{1,3}$",mail[1:])):
            valid = True

    if (valid):
        print(name+" "+dummy)
