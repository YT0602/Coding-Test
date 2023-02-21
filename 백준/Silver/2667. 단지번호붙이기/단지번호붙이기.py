from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
Q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
home = []


def BFS(r, c):
    global cnt
    Q.append((r, c))
    arr[r][c] = 0
    while Q:
        cx, cy = Q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 1:
                    cnt += 1
                    arr[nx][ny] = 0
                    Q.append((nx, ny))


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 1
            BFS(i, j)
            home.append(cnt)

home.sort()
if len(home) != 0:
    print(len(home))
    for i in home:
        print(i)
else:
    print(0)