import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))

start = min(T)
end = max(T) * M

result = 0 
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for t in T:
        cnt += mid // t

    if cnt >= M:
        result = mid
        end = mid -1
    else:
        start = mid + 1
        
print(result)