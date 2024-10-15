import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

unique_numbers = sorted(set(num_list))

result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(len(unique_numbers)):
        result.append(unique_numbers[i])
        dfs()
        result.pop()

dfs()
