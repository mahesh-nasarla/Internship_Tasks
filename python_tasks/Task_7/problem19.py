#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'weightedUniformStrings' function below.
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    previous_char = ''
    current_weight = 0

    for char in s:
        char_weight = ord(char) - ord('a') + 1

        if char == previous_char:
            current_weight += char_weight
        else:
            current_weight = char_weight
            previous_char = char

        weights.add(current_weight)

    result = []

    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
