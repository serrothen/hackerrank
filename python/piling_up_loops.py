#!/usr/bin/env python3

# Enter your code here. Read input from STDIN. Print output to STDOUT

# from collections import deque

ntest = int(input())

for _ in range(ntest):
    
    nblocks = int(input())
    blocks = list(map( int,input().split() ))
    
    index_l = 0
    index_r = nblocks-1
    index_l0 = index_l
    index_r0 = index_r
    locations = []
    flag_l = True
    flag_r = True

    if (blocks[index_l] >= blocks[index_r]):
        locations.append(index_l)
        index_l +=1
    else:
        locations.append(index_r)
        index_r -=1

    while (len(locations) != nblocks):
        
        # left path
        if (blocks[index_l]>=blocks[index_r] and blocks[index_l] <= blocks[locations[-1]] and flag_l==True):
            locations.append(index_l)
            index_l += 1
            flag_r = True
            continue
        # right path
        elif (blocks[index_l]<blocks[index_r] and blocks[index_r] <= blocks[locations[-1]] and flag_r==True):
            locations.append(index_r)
            index_r -= 1
            flag_l = True
            continue
        # no path works: go back one step
        else:
            # undo left step
            if (locations[-1]<index_l):
                # undo step
                locations.pop()
                index_l -= 1
                # prevent wrong step
                flag_l = False
            # undo right step
            elif (locations[-1]>index_r):
                # undo step
                locations.pop()
                index_r += 1
                # prevent wrong step
                flag_r = False
            # no path works
            if (index_l == index_l0 and index_r == index_r0):
                break

    if (len(locations) == nblocks):
        print("Yes")
    else:
        print("No")
