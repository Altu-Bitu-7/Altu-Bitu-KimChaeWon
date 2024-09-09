import sys
input = sys.stdin.readline

N = int(input())

num = 0
cnt = 0
while True:
    num += 1
    if '666' in str(num):
        cnt += 1

        if cnt == N:
            break

print(num)