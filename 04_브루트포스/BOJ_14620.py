from itertools import combinations

import sys
input = sys.stdin.readline

N = int(input())

flower=[]
all=[]

min_flower = 10000000

for _ in range(N):
    flower.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0] # 위 아래 왼 오
dy = [0, 0, -1, 1] 

def check(flower_list):
    global min_flower
    visited = []
    sum = 0
    for x,y in flower_list:
        visited.append((x,y))
        sum += flower[x][y]

        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if (xx, yy) not in visited:
                visited.append((xx,yy))
                sum += flower[xx][yy]
            else:
                return
            
    min_flower = min(min_flower, sum)
            

for i in range(1, N-1):
    for j in range(1, N-1):
        all.append((i,j))

for i in combinations(all, 3):
    check(i)

print(min_flower)