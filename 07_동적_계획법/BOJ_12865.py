import sys
input = sys.stdin.readline

N, K = map(int, input().split())  
weights = []
values = []

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

dp = [0] * (K + 1) 

for i in range(N):
    weight = weights[i]
    value = values[i]
    for w in range(K, weight - 1, -1):
        if dp[w - weight] + value > dp[w]:
            dp[w] = dp[w - weight] + value

print(dp[K]) 
