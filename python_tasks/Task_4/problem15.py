# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem: Word Order
# Link: https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

counts = Counter(words)

print(len(counts))
print(*counts.values())
