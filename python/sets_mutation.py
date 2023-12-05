#!/usr/bin/python3

# update(): adds elements to set
# intersction_update(): replace set with intersection of set with other set
# difference_update(): replace set with difference between set and other set
# symmetric_difference_update(): replace set with symmetric_difference between set and other set

num_a = int(input())
set_a = set(list(input().split()))

nsets = int(input())
for _ in range(nsets):
    command,num_i = list(input().split())
    set_i = set(list(input().split()))

    exec(f"set_a.{command}({set_i})")

print(sum(map(int,list(set_a))))
