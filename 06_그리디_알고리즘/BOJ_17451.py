import sys
import math
input = sys.stdin.readline

n = int(input())
planet = list(map(int, input().split()))

planet = list(reversed(planet))

first = planet[0]

for i in range(n):
    if planet[i] >= first:
        first = planet[i]
    else:
        first = planet[i] * math.ceil(first / planet[i])

print(first)