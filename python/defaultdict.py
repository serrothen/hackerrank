# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)

n,m = list(map(int,input().split()))

for ii in range(n):
    entry = input()
    d[entry].append(ii+1)
    
for ii in range(m):
    entry = input()
    lst = d[entry]
    if not lst:
        print(-1)
    else:
        for l in lst:
            print(l,end=" ")
        print("")
