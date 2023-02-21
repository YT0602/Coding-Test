from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
pic = []
cnt = 0

def BFS(r, c):
    global cnt
    Q.append((r, c))
    while Q:
        cx, cy = Q.popleft()
        arr[cx][cy] = 0
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    cnt += 1
                    Q.append((nx, ny))
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt = 1
            BFS(i, j)
            pic.append(cnt)

if len(pic) != 0:
    print(len(pic))
    print(max(pic))
else:
    print(0)
    print(0)