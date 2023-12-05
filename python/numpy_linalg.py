#!/usr/bin/env python3

import numpy

dim_n = int(input())
lst = []
for _ in range(dim_n):
    lst_tmp = list(map(float,input().split()))
    lst.append(lst_tmp)
arr_a = numpy.array(lst)

det_a = numpy.linalg.det(arr_a)
print(round(det_a,2))
