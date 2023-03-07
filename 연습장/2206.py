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
    # 0이면 안뚫었을 때, 1이면 한번 뚫은 경우
    vis[r][c][ch] = 1
    while q:
        cx, cy, ch = q.popleft()
        # 현재위치가 도착지면 종료
        if (cx, cy) == (N-1, M-1):
            ans = vis[cx][cy][ch]
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 길이 있고, 방문하지 않았으면 진행
                if arr[nx][ny] == 0 and vis[nx][ny][ch] == 0:
                    vis[nx][ny][ch] = vis[cx][cy][ch] + 1
                    q.append((nx, ny, ch))
                # 길이 없을때 아직 벽 안뚫었으면, 뚫고 진행
                elif arr[nx][ny] == 1 and ch == 0:
                    vis[nx][ny][1] = vis[cx][cy][0] + 1
                    q.append((nx, ny, 1))


BFS(0, 0, 0)

for i in vis:
    print(i)
print(ans)