import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

wheels = []

for i in range(T):
    wheel = deque(map(int, input().strip()))
    wheels.append(wheel)

K = int(input())

for _ in range(K):
    dict = {}
    num, direction = map(int, input().split())
    num -= 1 

    dict[num] = direction 

    min_num, max_num = num, num

    while True:
        changed = False
        if min_num > 0:
            if wheels[min_num][6] != wheels[min_num - 1][2]:
                dict[min_num - 1] = -dict[min_num]
                min_num -= 1
                changed = True
        if max_num < T - 1:
            if wheels[max_num][2] != wheels[max_num + 1][6]:
                dict[max_num + 1] = -dict[max_num]
                max_num += 1
                changed = True
        if not changed:
            break

    for i in dict.keys():
        if dict[i] == 1:
            wheels[i].appendleft(wheels[i].pop())
        elif dict[i] == -1:
            wheels[i].append(wheels[i].popleft())

cnt = 0
for i in range(T):
    if wheels[i][0] == 1:
        cnt += 1

print(cnt)