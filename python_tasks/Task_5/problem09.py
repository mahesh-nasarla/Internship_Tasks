# Problem: Word Order
# https://www.hackerrank.com/challenges/word-order/problem
from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]

counts = Counter(words)

print(len(counts))
print(*counts.values())
