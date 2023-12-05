#!/usr/bin/env python3

import numpy

dim_n,dim_m = list(map(int,input().split()))

lst = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst.append(lst_tmp)
arr = numpy.array(lst)

arr_sum = numpy.sum(arr,axis=0)
print(numpy.prod(arr_sum))
