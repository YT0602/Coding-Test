import sys
input = sys.stdin.readline

def back():
    if len(stack) == M+1:
        print(' '.join(map(str, stack[1:])))
        return
    for i in numbers:
        if i not in stack:
            if i > stack[len(stack)-1]:
                stack.append(i)
                back()
                stack.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
stack = [0]
numbers.sort()
back()