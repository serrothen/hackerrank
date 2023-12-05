#!/usr/bin/env python3

x,k = list(map(int,input().split()))
poly = input()

result = eval(poly)

print(result==k)
