N, M = map(int, input().split())

s = set()

for _ in range(N):
    s.add(input())

cnt = 0
for _ in range(M):
    if input() in s:
        cnt += 1

print(cnt)