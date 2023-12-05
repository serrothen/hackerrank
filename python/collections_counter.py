# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

nShoes = int(input())
listShoes = list(map(int,input().split()))
storage = Counter(listShoes)
nCustomer = int(input())

earnings = 0
for ii in range(nCustomer):
    size, price = list(map(int,input().split()))
    if (storage[size]>0):
        earnings += price
        storage[size] -=1

print(earnings)
