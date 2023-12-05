#!/usr/bin/env python3

import numpy

arr_a = numpy.array(list(map(int,input().split())))
arr_b = numpy.array(list(map(int,input().split())))

print(numpy.inner(arr_a,arr_b))
print(numpy.outer(arr_a,arr_b))
