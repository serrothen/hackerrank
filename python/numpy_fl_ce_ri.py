#!/usr/bin/env python3

import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array( list(map(float,input().split())) )

print(numpy.floor(arr))
print(numpy.ceil(arr))
# nearest integer
print(numpy.rint(arr))
