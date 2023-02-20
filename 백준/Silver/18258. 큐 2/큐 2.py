from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
d = deque()
for i in range(N):

    text = list(input().split())
    if text[0] == 'push':
        d.append(text[1])
    elif text[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif text[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    elif text[0] == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif text[0] == 'size':
        print(len(d))
    elif text[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
