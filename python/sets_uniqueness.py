#!/usr/bin/env python3

ntotal = int(input())

origins = []
for _ in range(ntotal):
    origins.append(input())

unique_origins = list(set(origins))
print(len(unique_origins))
