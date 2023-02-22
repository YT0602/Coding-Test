from collections import deque

def BFS(r, c):
    Q.append((r, c))
    global ans
    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == 0:
                    Q.append((nx, ny))
                    arr[nx][ny] = 1
                elif arr[nx][ny] == 3:
                    ans = 1


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    Q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    BFS(1, 1)
    print(f'#{tc} {ans}')