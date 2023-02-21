from collections import deque

def BFS(r, c):
    global ans
    Q.append((r, c))
    arr[r][c] = 1
    while Q:
        cx, cy = Q.popleft()
        arr[cx][cy] = 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[nx][ny] == 3:
                    ans = 1
                    return
                elif arr[nx][ny] == 0:
                    Q.append((nx, ny))


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    Q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    BFS(1, 1)
    print(f'#{tc} {ans}')