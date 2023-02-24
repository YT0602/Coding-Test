from collections import deque

def BFS():
    global ans
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[cx][cy] + 1
                        q.append((nx, ny))
                        ans += visited[nx][ny]
                    else:

                        if visited[nx][ny] - visited[cx][cy] >= 2:
                            ans -= visited[nx][ny]
                            visited[nx][ny] = visited[cx][cy] + 1
                            ans += visited[nx][ny]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[1 if ch == 'W' else 0 for ch in input()] for _ in range(N)]
    # arr = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0
    ans = 0
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                visited[i][j] = -1
                for k in range(4):
                    nnx, nny = i + dx[k], j + dy[k]
                    if 0 <= nnx < N and 0 <= nny < M:
                        if arr[nnx][nny] == 0:
                            if visited[nnx][nny] == 0:
                                visited[nnx][nny] = 1
                                q.append((nnx, nny))
                                ans += 1


    BFS()
    print(f'#{tc} {ans}')