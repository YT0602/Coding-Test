import sys
input = sys.stdin.readline

def back():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    for i in range(1, N+1):
        stack.append(i)
        back()
        stack.pop()


N, M = map(int, input().split())
stack = []

back()