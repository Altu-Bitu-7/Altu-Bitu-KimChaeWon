import sys
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(9)]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
blocks = [set() for _ in range(9)]

empty_cells = []

for i in range(9):
    for j in range(9):
        num = grid[i][j]
        if num == 0:
            empty_cells.append((i, j))
        else:
            rows[i].add(num)
            cols[j].add(num)
            blocks[(i//3)*3 + (j//3)].add(num)

def solve(idx):
    if idx == len(empty_cells):
        for row in grid:
            print(' '.join(map(str, row)))
        sys.exit(0)
    x, y = empty_cells[idx]
    block_num = (x//3)*3 + (y//3)
    for num in range(1, 10):
        if num not in rows[x] and num not in cols[y] and num not in blocks[block_num]:
            grid[x][y] = num
            rows[x].add(num)
            cols[y].add(num)
            blocks[block_num].add(num)
            solve(idx+1)
            grid[x][y] = 0
            rows[x].remove(num)
            cols[y].remove(num)
            blocks[block_num].remove(num)

solve(0)
