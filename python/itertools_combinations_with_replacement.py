# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

sStr,kStr = list(input().split())
kVal = int(kStr)

sComb = list( combinations_with_replacement(sStr,kVal) )

sList = []
for entry in sComb:
    word=""
    list_entry = list(entry)
    list_entry.sort()
    for letter in list_entry:
        
        word+=letter
    sList.append(word)

sList.sort()

for entry in sList:
    print(entry)
