import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())

    score = []

    for _ in range(N):
        doc, inter = map(int,input().split())
        score.append([doc, inter])

    score.sort(key = lambda x: x[0])

    cnt = 1

    first_score = score[0][1]

    for i in range(1, N):
        if score[i][1] < first_score:
            cnt += 1
            first_score = score[i][1]

    print(cnt)