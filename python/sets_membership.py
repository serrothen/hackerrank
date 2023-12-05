#!/usr/bin/env python3

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
set_a = set(list(map(int,input().split())))
set_b = set(list(map(int,input().split())))

happiness = 0
for entry in arr:
    if (entry in set_a):
        happiness +=1
    elif (entry in set_b):
        happiness -=1

print(happiness)
