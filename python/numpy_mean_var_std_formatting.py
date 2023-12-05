#!/usr/bin/env python3

import numpy

dim_n,dim_m = list(map(int,input().split()))
lst = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst.append(lst_tmp)
arr = numpy.array(lst)

mean = numpy.mean(arr,axis=1)
var = numpy.var(arr,axis=0)
std = numpy.std(arr)

print(numpy.array(mean))
print(numpy.array(var))
print(round(std,11))
