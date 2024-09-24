N = int(input())
h = list(map(int, input().split()))

sum_h = sum(h)
if sum_h % 3 != 0:
    print("NO")
else:
    S = sum_h // 3
    total_max_c2 = sum(hi // 2 for hi in h)
    if total_max_c2 < S:
        print("NO")
    else:
        print("YES")