# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

nLines = int(input())

regex_pattern = r".*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}).*"
for _ in range(nLines):
    line = input().split()
    lenLine = len(line)
    for iword in range(1,lenLine):
        m = re.match(regex_pattern,line[iword])
        if (m!=None):
            print(m.group(1))
