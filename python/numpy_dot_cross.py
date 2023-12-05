#!/usr/bin/env python3

import numpy

dim_n = int(input())
lst = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst.append(lst_tmp)
arr_a = numpy.array(lst)
lst = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst.append(lst_tmp)
arr_b = numpy.array(lst)

arr_c = numpy.zeros((dim_n,dim_n),dtype=int)
for col in range(numpy.shape(arr_b)[1]):
    for row in range(numpy.shape(arr_a)[0]):
        arr_c[row,col] = numpy.dot(arr_a[row,:],arr_b[:,col])

print(arr_c)
