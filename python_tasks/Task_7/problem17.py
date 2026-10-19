#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    # Write your code here
    for length in range(1, len(s) // 2 + 1):
        first = s[:length]

        if first[0] == '0':
            continue

        current = first
        next_number = int(first) + 1

        while len(current) < len(s):
            current += str(next_number)
            next_number += 1

        if current == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
