N = int(input())
serial = []

for _ in range(N):
    serial.append(input())

# 모든 자리수의 합을 더하는 함수
def sum_of_digits(s):
    sum = 0
    for digit in s:
        if digit.isdigit():
            sum += int(digit)
    return sum

serial.sort(key = lambda x: (len(x), sum_of_digits(x), x))

for s in serial:
    print(s)