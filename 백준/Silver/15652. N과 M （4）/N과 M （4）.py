import sys
input = sys.stdin.readline

def back():
    if len(stack) == M+1:
        print(' '.join(map(str, stack[1:])))
        return
    for i in range(1, N+1):
        if i >= stack[len(stack)-1]:
            stack.append(i)
            back()
            stack.pop()


N, M = map(int, input().split())
stack = [0]

back()