import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

circle = deque()
circle_delete = []

# for i in range(1,N+1):
#     circle.append(i)

circle = deque(range(1, N + 1))


while len(circle) != 0:
     for i in range(1,K+1):
        if i == K:
            circle_delete.append(circle.popleft())
        else:
            circle.append(circle.popleft())

print("<", end="")
print(", ".join(map(str, circle_delete)), end="")
print(">")