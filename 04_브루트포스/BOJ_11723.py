import sys
input = sys.stdin.readline

N = int(input())

s = set()

for _ in range(N):
    op = input().split()

    if len(op) == 1:
        if op[0] == 'all':
            s = set(range(1, 21))
        else:
            s.clear()
        continue

    command, num = op[0], int(op[1])

    if command == 'add':
        s.add(num)
    elif command == 'remove':
        s.discard(num)
    elif command == 'check':
        print(1 if num in s else 0)
    elif command == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)