import sys
input = sys.stdin.readline

N = int(input())

num_list= list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))