# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

listA = list(map(int,input().split()))
listB = list(map(int,input().split()))

listAxB = list(product(listA,listB))

for entry in listAxB:
    print(entry,end=" ")
print("")
