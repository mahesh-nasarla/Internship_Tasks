# Problem: Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
a = set(map(int, input().split()))
number_of_operations = int(input())

for _ in range(number_of_operations):
    operation, size = input().split()
    other_set = set(map(int, input().split()))

    if operation == "update":
        a.update(other_set)
    elif operation == "intersection_update":
        a.intersection_update(other_set)
    elif operation == "difference_update":
        a.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)

print(sum(a))
