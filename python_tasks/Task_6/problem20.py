# Problem: Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
n = int(input())
for _ in range(n):
    phone_number = input().strip()

    if re.fullmatch(r"[789]\d{9}", phone_number):
        print("YES")
    else:
        print("NO")
