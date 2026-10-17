# Problem: Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        segment = string[i:i + k]
        seen = set()
        result = []

        for char in segment:
            if char not in seen:
                seen.add(char)
                result.append(char)

        print("".join(result))

if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
