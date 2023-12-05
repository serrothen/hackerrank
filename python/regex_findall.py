#!/usr/bin/env python3

import re

s = input()

vk_list = re.findall(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z][aeiouAEIOU][aeiouAEIOU]+(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])',s)
v_list = [entry[1:] for entry in vk_list]

if (len(v_list)>0):
    for entry in v_list:
        print(entry)
else:
    print(-1)
