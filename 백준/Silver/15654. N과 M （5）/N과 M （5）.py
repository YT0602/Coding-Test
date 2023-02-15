import sys
input = sys.stdin.readline

def back():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    for i in numbers:
        if i not in stack:
            stack.append(i)
            back()
            stack.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
stack = []
numbers.sort()
back()