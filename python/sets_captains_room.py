#!/usr/bin/env python3

knum = int(input())
room_numbers = list(input().split())

unique_rooms = set(room_numbers)
dict_occupation = {room:0 for room in list(unique_rooms) }

for guest in room_numbers:
    dict_occupation[guest] += 1

for room in unique_rooms:
    if (dict_occupation[room]==1): print(room)
