
# Problem: Find the Runner-Up Score!
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))

unique_scores = sorted(set(arr), reverse=True)
print(unique_scores[1])
