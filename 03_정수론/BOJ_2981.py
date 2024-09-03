import sys
import math

input = sys.stdin.readline

N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))

num.sort()

dif_num = []

# 숫자들 간 차이
for i in range(len(num)-1, 0, -1):
    dif_num.append(num[i]-num[i-1])

# 최대공약수 구하기
gcd = dif_num[0]
for i in range(1, len(dif_num)):
    gcd = math.gcd(dif_num[i], gcd)

result = []

# 약수 구하기
for i in range(1, int(gcd**0.5)+1):
    if gcd % i == 0:
        result.append(i)
        if i != gcd//i:
            result.append(gcd//i)

result.sort()

for i in range(1, len(result)):
    print(result[i], end = ' ')

print()