import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [0] + [int(input()) for _ in range(T)]  # 1부터 시작하는 인덱스 사용
dp = [[0]*(W+1) for _ in range(T+1)]

for t in range(1, T+1):
    for w in range(W+1):
        dp[t][w] = dp[t-1][w]

        if w > 0:
            dp[t][w] = max(dp[t][w], dp[t-1][w-1])
        current_position = 1 if w % 2 == 0 else 2

        if tree[t] == current_position:
            dp[t][w] += 1

result = max(dp[T])
print(result)
