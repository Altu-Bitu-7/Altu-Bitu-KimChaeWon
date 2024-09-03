import sys
N, K = map(int, (input().split(" ")))

d1 = ['?']*N

num = 0
check = True

for i in range(K):
    S, alpha = input().split(" ")
    S = int(S)
    num = (num + S) % N
    if d1[num] != '?':    # 이미 알파벳이 차있는 자리에 다시 넣으려고 할 때
        if d1[num] != alpha: 
            check = False
            break
        else:             # 그러나 넣을 자리에 있는 알파벳과 넣을 알파벳이 같다면 통과
            d1[num] = alpha
    else:
        d1[num] = alpha

for i in range(N):
    if d1[i] != '?':
        for j in range(i+1, N):
            if d1[i] == d1[j]:
                check = False

if check:
    for i in range(N):
        print(d1[num % N] , end='')
        if(num >= 0):
            num -= 1
        else:
            num += N-1
else:
    print('!')