#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the 'isValid' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def isValid(s):
    # Write your code here
    char_freq = Counter(s)
    freq_count = Counter(char_freq.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) > 2:
        return "NO"

    (freq1, count1), (freq2, count2) = freq_count.items()

    if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
        return "YES"

    if abs(freq1 - freq2) == 1:
        if freq1 > freq2 and count1 == 1:
            return "YES"
        if freq2 > freq1 and count2 == 1:
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
