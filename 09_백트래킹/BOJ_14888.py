import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split())) # 1 2 3 4 5 6
op = list(map(int, input().split())) # + - * //

max_num = -1e9
min_num = 1e9

def dfs(cnt, total, add, sub, mul, div):
    global max_num, min_num
    if cnt == N:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    
    if add:
        dfs(cnt + 1, total + lst[cnt], add - 1, sub, mul, div)
    if sub:
        dfs(cnt + 1, total - lst[cnt], add, sub - 1, mul, div)
    if mul:
        dfs(cnt + 1, total * lst[cnt], add, sub, mul - 1, div)
    if div:
        dfs(cnt + 1, int(total / lst[cnt]), add, sub, mul, div - 1)


dfs(1, lst[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)