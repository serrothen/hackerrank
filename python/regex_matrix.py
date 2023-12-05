#!/usr/bin/env python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

sentence = ""
for mm in range(m):
    for nn in range(n):
        sentence += matrix[nn][mm]

clean = re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])"," ",sentence)
        
print(clean)
