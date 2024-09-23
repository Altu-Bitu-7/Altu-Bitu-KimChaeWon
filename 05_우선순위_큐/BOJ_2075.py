import heapq
import sys
input = sys.stdin.readline

n = int(input())

n_list=[]

for _ in range(n):
    data = map(int, input().split())
    for num in sorted(data):
        if len(n_list) >= n:
            heapq.heappop(n_list)
        heapq.heappush(n_list, num)

print(n_list[0])