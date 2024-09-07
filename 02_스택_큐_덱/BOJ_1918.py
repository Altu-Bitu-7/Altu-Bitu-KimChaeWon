infix = list(input())
stack = []
postfix = ''

for s in infix:
    if s.isalpha():
        postfix += s
    else:
        if s == '+' or s == '-':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfix += stack.pop()
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

while stack:
    postfix += stack.pop()

print(postfix)