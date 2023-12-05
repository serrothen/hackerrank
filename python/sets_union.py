#!/usr/bin/env python3

n_english = int(input())
students_english = set(list(input().split()))
n_french = int(input())
students_french = set(list(input().split()))

readers = students_english.union(students_french)

print(len(readers))
