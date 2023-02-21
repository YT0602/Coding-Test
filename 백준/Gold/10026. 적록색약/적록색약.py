from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
cnt = 0
RG_cnt = 0


def BFS(r, c, color, target):
    Q.append((r, c))
    arr[r][c] = target
    while Q:
        cx, cy = Q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == color:
                    arr[nx][ny] = target
                    Q.append((nx, ny))


for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            BFS(i, j, arr[i][j], 'r')
            cnt += 1
        elif arr[i][j] == 'B':
            BFS(i, j, arr[i][j], 'b')
            cnt += 1
        elif arr[i][j] == 'G':
            BFS(i, j, arr[i][j], 'r')
            cnt += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'r':
            BFS(i, j, arr[i][j], 'R')
            RG_cnt += 1
        elif arr[i][j] == 'b':
            BFS(i, j, arr[i][j], 'B')
            RG_cnt += 1

print(cnt)
print(RG_cnt)