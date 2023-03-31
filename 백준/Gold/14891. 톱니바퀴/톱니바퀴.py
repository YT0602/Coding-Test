import sys
from collections import deque
input = sys.stdin.readline


def left(n, a, dir):
    if n <= 0:
        return
    # 회전전에 바퀴의 극 기억해놔야함 !!
    # 9시 방향 극
    g9 = gear[n - 1][6]
    # 3시 방향 극
    g3 = gear[n - 1][2]
    # 극이 다르면 회전
    if g3 != a:
        if dir == -1:
            gear[n - 1].appendleft(gear[n - 1].pop())
        else:
            gear[n - 1].append(gear[n - 1].popleft())
        left(n-1, g9, -dir)


def right(n, a, dir):
    if n >= 3:
        return

    # 9시 방향 극
    g9 = gear[n + 1][6]
    # 3시 방향 극
    g3 = gear[n + 1][2]

    # 극이 다르면 회전
    if g9 != a:
        if dir == -1:
            gear[n + 1].appendleft(gear[n + 1].pop())
        else:
            gear[n + 1].append(gear[n + 1].popleft())
        right(n+1, g3, -dir)


# 3시 방향 톱니 [2], 9시 방향 톱니 [6]
# -1: 반시계, 1: 시계
# 반시계 : append(popleft), 시계 : appendleft(pop)
# 0: N극, 1: S극
gear = [deque(map(int, input().strip())) for _ in range(4)]

K = int(input())
for _ in range(K):
    num, ro = map(int, input().split())
    # 9시 방향 극
    x = gear[num-1][6]
    # 3시 방향 극
    y = gear[num-1][2]
    if ro == -1:
        gear[num-1].append(gear[num-1].popleft())
    else:
        gear[num - 1].appendleft(gear[num - 1].pop())
    left(num-1, x, ro)
    right(num-1, y, ro)

ans = 0
for i in range(4):
    ans += gear[i][0] * 2**i

print(ans)
