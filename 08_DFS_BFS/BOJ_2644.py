import sys
input = sys.stdin.readline

n = int(input())
A,B = map(int, input().split())
m = int(input())

g = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split())

    g[a].append(b)
    g[b].append(a)

def dfs(g,n,visited, depth):
    visited[n] = True
    if n == B:
        return depth
    for i in g[n]:
        if not visited[i]:
            result = dfs(g,i,visited, depth+1)
            if result != -1:
                return result
    return -1

result = dfs(g, A, visited, 0)
print(result)