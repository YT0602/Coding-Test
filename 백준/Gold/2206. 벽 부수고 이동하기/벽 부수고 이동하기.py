import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
vis = [[[0]*2 for _ in range(M)] for _ in range(N)]
ans = -1


def BFS(r, c, ch):
    global ans
    q.append((r, c, ch))
    vis[r][c][ch] = 1
    while q:
        cx, cy, ch = q.popleft()

        if (cx, cy) == (N-1, M-1):
            ans = vis[cx][cy][ch]
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 and vis[nx][ny][ch] == 0:
                    vis[nx][ny][ch] = vis[cx][cy][ch] + 1
                    q.append((nx, ny, ch))
                elif arr[nx][ny] == 1 and ch == 0:
                    vis[nx][ny][1] = vis[cx][cy][0] + 1
                    q.append((nx, ny, 1))


BFS(0, 0, 0)

print(ans)