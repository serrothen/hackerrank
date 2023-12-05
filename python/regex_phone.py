# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

nlines = int(input())

for ii in range(nlines):
    number = input()
    m = re.match(r"^(7|8|9)[0-9]{9}$",number)
    if (m!=None):
        print("YES")
    else:
        print("NO")
