import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bottles = [1] * N

digit = 1
more = 0
bottles_num = N

while bin(bottles_num).count('1') > K: 
    if bottles_num % 2 == 1: 
        more += 2 ** (digit - 1)  
        bottles_num += 1 

    bottles_num //= 2 
    digit += 1

print(more)