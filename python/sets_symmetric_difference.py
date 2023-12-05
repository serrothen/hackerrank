#!/usr/bin/env python3

n_english = int(input())
students_english = set(list(input().split()))
n_french = int(input())
students_french = set(list(input().split()))

monolingual = students_english.symmetric_difference(students_french)
print(len(monolingual))
