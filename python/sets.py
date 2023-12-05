#!/usr/bin/env python3

m = input()
m_lst = list( map(int,input().split()) )
n = input()
n_lst = list( map(int,input().split()) )

m_set = set(m_lst)
n_set = set(n_lst)

union_nm = m_set.union(n_set)
intersect_nm = m_set.intersection(n_set)
xor_nm = union_nm.difference(intersect_nm)

xor_lst = list(xor_nm)
xor_lst.sort()

for element in xor_lst:
    print(element)
