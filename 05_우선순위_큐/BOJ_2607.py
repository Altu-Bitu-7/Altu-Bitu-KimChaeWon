import heapq
import sys
input = sys.stdin.readline

# 한 단어에서 한 문자 더하거나, 빼거나,
# 하나의 문자를 다른 문자로 바꾸어  

n = int(input())
cnt = 0

word = list(input().strip())

for i in range(n-1):
    s_cnt = 0
    compare = list(input().strip())

    for c in word[:]:
        if c in compare:
            compare.remove(c)
        else:
            s_cnt += 1

    if len(compare) < 2 and s_cnt < 2:
        cnt += 1

print(cnt)