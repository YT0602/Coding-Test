import sys
from collections import deque
input = sys.stdin.readline


def BFS(row, col):
    Q.append((row, col))
    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[cx][cy] + 1
                    Q.append((nx, ny))
                if nx == N-1 and ny == M-1:
                    return


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
cnt = 0
BFS(0, 0)

print(arr[N-1][M-1])