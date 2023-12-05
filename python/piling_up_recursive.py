#!/usr/bin/env python3

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

ntest = int(input())

def check_blocks(blocks,top):
    # print(blocks)
    if (not blocks):
        return True
    if (blocks[-1]<=top):
        top = blocks.pop()
        flag = check_blocks(blocks,top)
        if (flag):
            return flag
    if (blocks[0]<=top):
        top = blocks.popleft()
        flag = check_blocks(blocks,top)
        if (flag):
            return flag
    return False

for _ in range(ntest):
    nblocks = int(input())
    blocks = list(map( int,input().split() ))

    # right path
    # print("right")
    test_blocks = deque(blocks)
    top = test_blocks.pop()
    flag = check_blocks(test_blocks,top)

    if (not flag):
        # left path
        # print("left")
        test_blocks = deque(blocks)
        top = test_blocks.popleft()
        flag = check_blocks(test_blocks,top)

    if (flag):
        print("Yes")
    else:
        print("No")
