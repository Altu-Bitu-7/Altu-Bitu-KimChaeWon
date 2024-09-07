import sys
from collections import deque
input = sys.stdin.readline

mapping = {')': '(', ']': '['}

while True:
    sentence = input().rstrip()

    if sentence == ".":
        break

    stack = deque()
    result = "yes"

    for s in sentence:
        if s in mapping.values():
            stack.append(s)
        elif s in mapping.keys():
            if not stack or stack.pop() != mapping[s]:
                result = "no"
                break

    if stack:
        result = "no"

    print(result)