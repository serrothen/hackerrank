#!/usr/bin/env python3

num_st,num_sub = list(map(int,input().split()))

grades = []
for _ in range(num_sub):
    grades.append( list(map(float,input().split())) )

students = list(zip(*grades))

for st in students:
    av = sum(st)/num_sub
    print(f"{av:.1f}")

