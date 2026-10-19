#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    # Write your code here
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)

    if result:
        return result
    else:
        return "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
