import sys
input = sys.stdin.readline

K = int(input())

lst = []
for i in range(6):
    lst.append(list(map(int, input().split())))

max_area = 0
min_area = 0

for i in range(6):  
    area = lst[i][1] * lst[(i + 1) % 6][1]  
    if area > max_area:
        max_area = area
        max_i = lst[i][0]
        max_j = lst[(i + 1) % 6][0]

if max_i == 4 and max_j == 2:
    for i in range(6):
        if lst[i][0] == 1 and lst[(i + 1) % 6][0] == 3:
            min_area = lst[i][1] * lst[(i + 1) % 6][1]
elif max_i == 3 and max_j == 1:
    for i in range(6):
        if lst[i][0] == 2 and lst[(i + 1) % 6][0] == 4:
            min_area = lst[i][1] * lst[(i + 1) % 6][1]
elif max_i == 2 and max_j == 3:
    for i in range(6):
        if lst[i][0] == 4 and lst[(i + 1) % 6][0] == 1:
            min_area = lst[i][1] * lst[(i + 1) % 6][1]
elif max_i == 1 and max_j == 4:
    for i in range(6):
        if lst[i][0] == 3 and lst[(i + 1) % 6][0] == 2:
            min_area = lst[i][1] * lst[(i + 1) % 6][1]

print(K * (max_area-min_area))