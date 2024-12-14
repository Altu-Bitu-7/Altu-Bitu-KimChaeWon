import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_list = sorted(N_list)

start = 0
end = N-1

result = []

def binary_search(i):
    start = 0
    end = N-1
    find = False
    while start <= end:
        mid = (start + end) // 2

        if i == N_list[mid]:
            result.append("1")
            find = True
            break
        elif i < N_list[mid]:
            end = mid -1
        else:
            start = mid + 1

    if not find:
        result.append("0")

for num in M_list:
    binary_search(num)

print(' '.join(result))