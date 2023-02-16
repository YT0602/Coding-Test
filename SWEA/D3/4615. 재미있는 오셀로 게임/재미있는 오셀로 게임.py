def DFS(row, col, num, target):
    arr[row][col] = num
    for j in range(8):
        nx = row + dx[j]
        ny = col + dy[j]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == target:
            change(nx, ny, num, target, j)
    return


def change(row, col, num, target, direction):
    nx = row + dx[direction]
    ny = col + dy[direction]
    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == target:
        change(nx, ny, num, target, direction)
    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == num:
        arr[row][col] = num
        return
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    W_cnt = 0
    B_cnt = 0
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    for i in range(M):
        point = list(map(int, input().split()))
        if point[2] == 1:
            DFS(point[1]-1, point[0]-1, 1, 2)
        else:
            DFS(point[1] - 1, point[0] - 1, 2, 1)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                B_cnt += 1
            elif arr[i][j] == 2:
                W_cnt += 1
    print(f'#{tc} {B_cnt} {W_cnt}')