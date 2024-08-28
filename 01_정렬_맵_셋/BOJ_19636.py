import sys
import math
input = sys.stdin.readline

W, I, T = map(int, input().split())
D, I2, A = map(int, input().split())

# 일일 기초 대사량
I_C = I
# 체중
W_C = W

# 일일 기초 대사량 변화 고려 x
for i in range(D):
    W = W + (I2 - (I + A))
    if (W <= 0 or I <= 0):
        print('Danger Diet')
        break

else:
    print(W, I)

# 일일 기초 대사량 변화 고려
for i in range(D):
    W_C = W_C + (I2 - (I_C + A))
    if abs(I2 - (I_C + A)) > T :
        I_C = I_C + math.floor((I2 - (I_C + A))/2)
    if (W_C <= 0 or I_C <= 0):
        print('Danger Diet')
        break

else:
    if (I - (I_C)) > 0:
        yoyo = 'YOYO'
    else:
        yoyo = 'NO'
    print(W_C, I_C, yoyo)