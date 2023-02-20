import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
move = deque()
visited = [0] * 100001


def seek(num):
    global cnt
    move.append(num)
    while move:
        cnt += 1
        x = move.popleft()
        if x == K:
            return
        can_move = [x-1, x+1, x*2]
        for i in can_move:
            if 0 <= i <= 100000 and visited[i] == 0:
                move.append(i)
                visited[i] = visited[x]+1


seek(N)
print(visited[K])