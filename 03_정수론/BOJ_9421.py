import sys
input = sys.stdin.readline

N = 1000001
array = [True] * N

n=int(input())

for i in range(3, int(len(array) ** 0.5) + 1, 2):
    if array[i]:
        for j in range(i*2, N, i):
            array[j] = False
    
def sang(num):
    visited = set()  
    while num != 1 and num not in visited:
        visited.add(num)
        num = sum(int(digit) ** 2 for digit in str(num)) 
    return num == 1

for i in range(3, n, 2):
    if array[i] and sang(i):
        print(i)