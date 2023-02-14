import sys
input = sys.stdin.readline

lazer = list(input())
stack = []
# 잘린 조각
seg = 0
for i in range(len(lazer)):
    if lazer[i] == '(':
        if lazer[i+1] == ')':
            seg += len(stack)
        else:
            seg += 1
            stack.append('(')
    elif lazer[i] == ')':
        if lazer[i-1] == '(':
            continue
        else:
            stack.pop()

print(seg)