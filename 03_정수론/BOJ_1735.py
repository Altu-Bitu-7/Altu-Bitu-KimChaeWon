import sys
import math
input = sys.stdin.readline

A,B = map(int, input().split())
C,D = map(int, input().split())

new_mom = B*D
new_A = A*D
new_C = C*B
new_son = new_A + new_C


while True:
    gcd = math.gcd(new_son, new_mom)
    if gcd != 1:
        new_son = new_son//gcd
        new_mom = new_mom//gcd
    else:
        break

print(new_son, new_mom)