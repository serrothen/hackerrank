# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

sStr,kStr = input().split()

kVal = int(kStr) 
sList = list(sStr)

sPerm = list(permutations(sList,kVal))

sList = []
for entry in sPerm:
    word = ""
    for letter in entry:
        word+=letter
    sList.append(word)

sList.sort()

for entry in sList:
    print(entry)

