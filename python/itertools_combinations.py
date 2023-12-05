# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

sStr,kStr = input().split()
kVal = int(kStr)

sList = []
for ik in range(1,kVal+1):
    sComb = list(combinations(sStr,ik))
    wordList = []
    for entry in sComb:
        word=""
        list_entry = list(entry)
        list_entry.sort()
        for letter in list_entry:
            word+=letter
        wordList.append(word)
    wordList.sort()
    sList.append(wordList)
    
sFlat = [item for sublist in sList for item in sublist]

for word in sFlat:
    print(word)


