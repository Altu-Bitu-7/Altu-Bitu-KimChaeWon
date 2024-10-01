import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dosu = [deque(), deque()]
ground = [deque(), deque()]

for _ in range(N):
    dodo, suyeon = map(int, input().split())
    dosu[0].append(dodo)
    dosu[1].append(suyeon)

start = 0
for _ in range(M):
    ground[start].append(dosu[start].pop())
    if not dosu[0] or not dosu[1]: # 비어있으면
        break
    winner = -1
    if ground[start] and ground[start][-1] == 5:
        winner = 0
    if ground[start] and ground[1-start] and ground[start][-1] + ground[1-start][-1] == 5:
        winner = 1
    if winner != -1:
        # 상대방 -> 내꺼 순으로
        for i in [1 - winner, winner]:
            while ground[i]:
                dosu[winner].appendleft(ground[i].popleft())
    start = 1 - start

if len(dosu[0]) > len(dosu[1]):
    print('do')
elif len(dosu[0]) < len(dosu[1]):
    print('su')
else:
    print('dosu')