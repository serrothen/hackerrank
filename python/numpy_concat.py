#!/usr/bin/env python3

import numpy

dim_n,dim_m,dim_p = list(map(int,input().split()))

lst_n = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst_n.append(lst_tmp)
arr_n = numpy.array(lst_n)

lst_m = []
for _ in range(dim_m):
    lst_tmp = list(map(int,input().split()))
    lst_m.append(lst_tmp)
arr_m = numpy.array(lst_m)

print( numpy.concatenate((arr_n,arr_m)) )
