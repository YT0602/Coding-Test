def DFS(r, c, cnt):
    global ans

    if r == c == N-1:
        ans = min(ans, cnt)
        return
    # 최소합보다 값이 커지면 중단
    if cnt > ans:
        return
    # 아래, 오른쪽 두가지 경우만 가능
    for dx, dy in ((1, 0), (0, 1)):
        nx = r + dx
        ny = c + dy
        if 0 <= nx < N and 0 <= ny < N:
            # 현재 위치값 더하면서 재귀 호출
            DFS(nx, ny, cnt + arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 251
    DFS(0, 0, arr[0][0])

    print(f'#{tc} {ans}')