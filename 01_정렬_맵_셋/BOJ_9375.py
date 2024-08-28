import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    dict = {}

    for _ in range(n):
        name, type = input().split()
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1

    case = 1
    for cnt in dict.values():
        case *= (cnt + 1)

    print(case-1)