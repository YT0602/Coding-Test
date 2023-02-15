import string
N = int(input())
cal = list(input())
num = [int(input()) for _ in range(N)]
alpha = string.ascii_uppercase
stack = []
for i in cal:
    if i.isalpha():
        i = num[alpha.index(i)]
        stack.append(i)
    else:
        y = stack.pop()
        x = stack.pop()
        if i == '*':
            stack.append(x * y)
        elif i == '/':
            stack.append(x / y)
        elif i == '+':
            stack.append(x + y)
        elif i == '-':
            stack.append(x - y)
ans = stack.pop()
print(f'{ans:.2f}')