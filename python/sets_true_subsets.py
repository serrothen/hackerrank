#!/usr/bin/env python3

set_a = set(list(input().split()))
num_sets = int(input())
subset_flag = True

for _ in range(num_sets):
    set_i = set(list(input().split()))
    set_b = set_i.intersection(set_a)
    if (set_i == set_b and set_a != set_b):
        continue
    else:
        subset_flag = False
        break

print(subset_flag)
