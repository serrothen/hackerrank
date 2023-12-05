#!/usr/bin/env python3

def split_and_join(line):
    # write your code here
    dummy = line.split(" ")
    result = "-".join(dummy)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
