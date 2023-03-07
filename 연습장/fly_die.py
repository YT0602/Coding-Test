def plus_spray(r, c, x):
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if x < M-1:
        cnt = plus_spray(r, c, x + 1)
        for k in range(4):
            nx = r + dx[k]*(x+1)
            ny = c + dy[k]*(x+1)
            if 0 <= nx < N and 0 <= ny < N:
                cnt += arr[nx][ny]

    return cnt


def x_spray(r, c, x):
    cnt = 0

    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    if x < M-1:
        cnt = x_spray(r, c, x + 1)
        for k in range(4):
            nx = r + dx[k]*(x+1)
            ny = c + dy[k]*(x+1)
            if 0 <= nx < N and 0 <= ny < N:
                cnt += arr[nx][ny]

    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(1, N-1):
        for j in range(1, N-1):
            ans = max(x_spray(i, j, 0)+arr[i][j], plus_spray(i, j, 0)+arr[i][j], ans)
    print(f'#{tc} {ans}')