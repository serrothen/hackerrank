#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    nameList = s.split(" ")
    nameLen = len(nameList)
    nameOut=""
    for ii in range(nameLen-1):
        nameOut += nameList[ii].capitalize()+" "
    nameOut += nameList[nameLen-1].capitalize()
    return nameOut

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

