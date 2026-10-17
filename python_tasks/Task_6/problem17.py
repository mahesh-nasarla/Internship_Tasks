# Problem: Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other_set = set(map(int, input().split()))

    if not set_a > other_set:
        result = False
        break

print(result)
