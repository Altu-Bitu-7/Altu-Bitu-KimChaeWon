import sys
input = sys.stdin.readline

stair = []
N = int(input())

for _ in range(N):
    stair.append(int(input()))

dp = [[0, 0] for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[0][0] = stair[0]
        dp[0][1] = stair[0]
    elif i == 1:
        dp[1][0] = stair[1]
        dp[1][1] = dp[0][0] + stair[1]
    else:
        dp[i][0] = max(dp[i-2]) + stair[i]
        dp[i][1] = dp[i-1][0] + stair[i]

print(max(dp[N-1]))