import sys
input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split())) 

new_list = [-1] * N
stack = []

for i in range(len(num_list)):
    while stack and (num_list[i] > num_list[stack[-1]]):
        new_list[stack.pop()] = num_list[i]
        
    stack.append(i)

print(' '.join(map(str, new_list)))