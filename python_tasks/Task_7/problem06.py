#!/bin/python3

# Problem: pangram's problem
# https://www.hackerrank.com/challenges/pangram's/problem
import math
import os
import random
import re
import sys
# Complete the 'pangrams' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def pangrams(s):
    # Write your code here
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    if alphabet.issubset(set(s.lower())):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
