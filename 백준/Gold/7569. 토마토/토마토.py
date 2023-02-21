from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
Q = deque()
ans = 1


def BFS(y, r, c):
    while Q:
        cz, cx, cy = Q.popleft()
        for l in range(6):
            nz = cz + dz[l]
            nx = cx + dx[l]
            ny = cy + dy[l]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if arr[nz][nx][ny] == 0:
                    Q.append((nz, nx, ny))
                    arr[nz][nx][ny] = arr[cz][cx][cy] + 1


def check(arr):
    global ans
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    ans = -1
                    return
                else:
                    if arr[i][j][k] > ans:
                        ans = arr[i][j][k]


for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                Q.append((i, j, k))


BFS(0, 0, 0)

check(arr)
if ans < 0:
    print(ans)
else:
    print(ans-1)