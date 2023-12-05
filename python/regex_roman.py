#!/usr/bin/env python3

regex_pattern = r"^M{0,3}(CM|CD|D){0,1}C{0,2}(C|XC){0,1}(XL|L){0,1}X{0,2}(IX|X){0,1}(IV|V){0,1}I{0,3}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
