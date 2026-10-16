
# Problem: Lists
# Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == "__main__":
    N = int(input())
    result = []

    for _ in range(N):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            result.insert(int(command[1]), int(command[2]))
        elif operation == "print":
            print(result)
        elif operation == "remove":
            result.remove(int(command[1]))
        elif operation == "append":
            result.append(int(command[1]))
        elif operation == "sort":
            result.sort()
        elif operation == "pop":
            result.pop()
        elif operation == "reverse":
            result.reverse()
