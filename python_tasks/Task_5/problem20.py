# Problem: Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque
for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    last = float("inf")
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            chosen = blocks.popleft()
        else:
            chosen = blocks.pop()

        if chosen > last:
            possible = False
            break

        last = chosen

    print("Yes" if possible else "No")
