# Problem: The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
rooms = list(map(int, input().split()))

room_counts = {}

for room in rooms:
    room_counts[room] = room_counts.get(room, 0) + 1

for room, count in room_counts.items():
    if count == 1:
        print(room)
        break
