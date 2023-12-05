#!/usr/bin/env python3

import numpy

dim_n,dim_m = list(map(int,input().split()))
lst = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst.append(lst_tmp)
arr = numpy.array(lst)

mins = numpy.min(arr,axis=1)
maxs = numpy.max(mins)
print(maxs)
