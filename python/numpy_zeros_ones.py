#!/usr/bin/env python3

import numpy

dimensions = list(map(int,input().split()))

arr_zeros = numpy.zeros(dimensions,dtype=int)
arr_ones = numpy.ones(dimensions,dtype=int)

print(arr_zeros)
print(arr_ones)
