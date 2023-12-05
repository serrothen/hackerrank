#!/usr/bin/env python3

# Enter your code here. Read input from STDIN. Print output to STDOUT

# from collections import deque

ntest = int(input())

for _ in range(ntest):
    
    nblocks = int(input())
    blocks = list(map( int,input().split() ))
    
    index_l = 0
    index_r = nblocks-1
    nlocation = 0

    if (blocks[index_l] >= blocks[index_r]):
        location = index_l
        index_l += 1
        nlocation += 1
    else:
        location = index_r
        index_r -= 1
        nlocation += 1

    while (nlocation != nblocks):
        
        # left path
        if (blocks[index_l]>=blocks[index_r] and blocks[index_l] <= blocks[location]):
            location = index_l
            index_l += 1
            nlocation += 1
            continue
        # right path
        elif (blocks[index_l]<blocks[index_r] and blocks[index_r] <= blocks[location]):
            location = index_r
            index_r -= 1
            nlocation += 1
            continue
        # no path works: go back one step
        else:
            break

    if (nlocation == nblocks):
        print("Yes")
    else:
        print("No")
