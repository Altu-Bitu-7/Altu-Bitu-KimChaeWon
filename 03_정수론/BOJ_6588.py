import sys

n = 1000001
array=[True]*n

for i in range(3, int(len(array) ** 0.5) + 1, 2):
    if array[i]:
        for j in range(i*2, n, i):
            array[j] = False

while True:
    num = int(sys.stdin.readline())
    if num ==  0:
        break
    for i in range(3, int(num/2) + 1, 2):
        if array[i] and array[num-i]: #최대한 i가 작은 값이여야 하므로 
            #작은 값부터 반복문 시작해서 둘 다 소수인 처음 경우가 답이됨
            print(f'{num} = {i} + {num-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")