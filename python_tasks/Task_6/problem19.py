#!/bin/python3
# Problem: Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    result = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    for char, count in result[:3]:
        print(char, count)
