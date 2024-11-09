import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False] * (N+1)
g = [[] for i in range(N+1)]


for _ in range(M):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

def dfs(g, v, visited):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(g, i, visited)

dfs(g, 1, visited)

cnt = 0
for i in range(N+1):
    if visited[i] == True:
        cnt += 1

print(cnt - 1)