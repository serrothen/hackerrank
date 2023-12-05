#!/usr/bin/env python3

import numpy

dim_n,dim_m = list(map(int,input().split()))

lst_a = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst_a.append(lst_tmp)
arr_a = numpy.array(lst_a)

lst_b = []
for _ in range(dim_n):
    lst_tmp = list(map(int,input().split()))
    lst_b.append(lst_tmp)
arr_b = numpy.array(lst_b)

print(arr_a + arr_b)
print(arr_a - arr_b)
print(arr_a * arr_b)
print(arr_a // arr_b)
print(arr_a % arr_b)
print(arr_a**arr_b)
