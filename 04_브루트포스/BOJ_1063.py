import sys
input = sys.stdin.readline

king, stone, N = input().split()

col_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}

change_list = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

king_i, king_j = ord(king[0]) - ord('A') + 1, int(king[1])
stone_i, stone_j = ord(stone[0]) - ord('A') + 1, int(stone[1])

for _ in range(int(N)):
    idx = change_list.index(input().strip())

    new_king_i, new_king_j = king_i + dx[idx], king_j + dy[idx]

    if 0 < new_king_i <= 8 and 0 < new_king_j <= 8:
        if new_king_i == stone_i and new_king_j == stone_j:
            new_stone_i, new_stone_j = stone_i + dx[idx], stone_j + dy[idx]
            if 0 < new_stone_i <= 8 and 0 < new_stone_j <= 8:
                stone_i, stone_j = new_stone_i, new_stone_j
            else:
                continue  # 돌이 범위를 벗어나면 킹도 움직이지 않음
        king_i, king_j = new_king_i, new_king_j

print(col_dict[king_i] + str(king_j))
print(col_dict[stone_i] + str(stone_j))