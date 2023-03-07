def pang(r, c):
    cnt = 0
    cnt += arr[r][c]
    for x in range(4):
        for k in range(1, arr[r][c]+1):
            nx = r + dx[x]*k
            ny = c + dy[x]*k
            if 0 <= nx < N and 0 <= ny < M:
                cnt += arr[nx][ny]
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            mx = max(mx, pang(i, j))
    print(f'#{tc} {mx}')