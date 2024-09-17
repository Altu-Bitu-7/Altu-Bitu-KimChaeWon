import heapq
import sys
input = sys.stdin.readline

n = int(input())

present = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0:
        if len(present) != 0:
            print(-heapq.heappop(present))
        else:
            print(-1)
    else:
        for i in range(len(a)-1):
            heapq.heappush(present, -a[i+1])