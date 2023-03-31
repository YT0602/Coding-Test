def tour(si, sj, r, c, dir, cnt):
    global ans
 
    # 방향전환 4번 미만까지
    for k in range(dir, 4):
        nx = r + move[dir][0]
        ny = c + move[dir][1]
        # 방향바꿨을때 처음위치면
        if nx == si and ny == sj:
            # 방문 카페가 3곳 이상이면 비교
            if cnt > 2:
                ans = max(ans, cnt)
                return
            continue
        # 범위 안이고 방문 안했으면 추가
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and v[arr[nx][ny]] == 0:
            # 방문 추가하고 재귀
            v[arr[nx][ny]] = 1
            tour(si, sj, nx, ny, k, cnt + 1)
            v[arr[nx][ny]] = 0
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * 101
    ans = -1
    # 이동순서
    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    # 방향
    dir = 0
    # 사각형 만들어야 되므로 범위 제한
    for i in range(N-2):
        for j in range(1, N-1):
            v[arr[i][j]] = 1
            tour(i, j, i, j, dir, 1)
            v[arr[i][j]] = 0
 
    print(f'#{tc} {ans}')