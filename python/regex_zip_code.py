#!/usr/bin/env python3

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(?P<m1>[0-9]).(?P=m1))"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
