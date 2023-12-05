#!/usr/bin/env python3

n = int(input())
s = set(map(int, input().split()))
ncommands = int(input())

for _ in range(ncommands):
    line = input().split()
    command = line[0]
    if (len(line)==1):
        exec(f"s.{command}()")
    if (len(line)>1):
        position = int(line[1])
        exec(f"s.{command}({position})")

print(sum(list(s)))

