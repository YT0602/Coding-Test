from collections import deque
import sys
input = sys.stdin.readline


A, B = map(int, input().split())
cnt = {}
Q = deque()


def search(n, target):
    Q.append(n)
    cnt[n] = 1
    while Q:
        x = Q.popleft()
        lst = [x * 2, x * 10 + 1]
        last = cnt[x]
        for i in lst:
            if i <= B:
                cnt.setdefault(i, 0)
                cnt[i] = last + 1
                Q.append(i)
            if i == target:
                return


search(A, B)
try:
    print(cnt[B])

except:
    print(-1)