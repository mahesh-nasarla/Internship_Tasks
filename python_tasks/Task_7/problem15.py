#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gameOfThrones' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def gameOfThrones(s):
    # Write your code here
    odd_count = 0

    for char in set(s):
        if s.count(char) % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
