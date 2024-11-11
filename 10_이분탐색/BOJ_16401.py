import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, max(snacks)

result = 0 

while start <= end:
    mid = (start + end) // 2

    count = sum(snack // mid for snack in snacks)

    if count >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)