import sys
input = sys.stdin.readline

name = input().strip()

dict = {}

front = ''
mid = ''
odd = 0

for n in name:
    dict[n] = dict.get(n, 0) + 1

for key in sorted(dict.keys()):
    count = dict[key]
    if count % 2 == 1:
        odd += 1
        mid = key

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    for key in sorted(dict.keys()):
        front +=  key * (dict[key] // 2)
    result = front + mid + front[::-1]
    print(result)