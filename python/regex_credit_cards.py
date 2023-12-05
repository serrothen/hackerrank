#!/usr/bin/env python3

import re

nCards = int(input())

for _ in range(nCards):
    number = input()

    if (re.match(r"^[456][0-9]{15}$",number) and
        not re.match(r".*(0{4}|1{4}|2{4}|3{4}|4{4}|5{4}|6{4}|7{4}|8{4}|9{4}).*",number)):
        print("Valid")
    elif (re.match(r"^[456]([0-9]){3}-([0-9]){4}-([0-9]){4}-([0-9]){4}$",number)):
        numberList = number.split("-")
        numberStr = ""
        for block in numberList:
            numberStr += block
        if (not re.match(r".*(0{4}|1{4}|2{4}|3{4}|4{4}|5{4}|6{4}|7{4}|8{4}|9{4}).*",numberStr)):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
