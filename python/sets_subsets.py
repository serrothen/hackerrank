#!/usr/bin/env python3

num_t = int(input())

for _ in range(num_t):
    num_a = int(input())
    set_a = set(list(input().split()))
    num_b = int(input())
    set_b = set(list(input().split()))

    print(set_b.intersection(set_a) == set_a)
