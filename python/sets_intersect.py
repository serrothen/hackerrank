#!/usr/bin/env python3

n_english = int(input())
students_english = set(list(input().split()))
n_french = int(input())
students_french = set(list(input().split()))

multilingual = students_english.intersection(students_french)
print(len(multilingual))
