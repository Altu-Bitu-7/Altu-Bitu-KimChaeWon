import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

cnt = 0

if sum(height) % 3 != 0:
    print("NO")
else:
    for h in height:
        cnt += h//2
    if cnt < sum(height) // 3:
        print("NO")
    else:
        print("YES")