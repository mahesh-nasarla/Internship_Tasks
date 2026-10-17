# Problem: Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

test_cases = int(input())

for _ in range(test_cases):
    a_count = int(input())
    set_a = set(map(int, input().split()))

    b_count = int(input())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))
