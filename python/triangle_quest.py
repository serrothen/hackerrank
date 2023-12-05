#!/usr/bin/env python3

for ii in range(1,int(input())+1):
    print(*range(1,ii),*range(ii,0,-1),sep='')
