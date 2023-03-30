def tour(si, sj, r, c, dir):
    global ans
    # 방향바꿨을때 처음위치면
    if dir == 3 and r == si and c == sj:
        # 방문 카페가 3곳 이상이면 비교
        if len(cafe) > 2:
            ans = max(ans, len(cafe))
        return

    if dir > 3:
        return
    # 방향전환 4번 미만까지
    for k in range(dir, 5):
        nx = r + move[dir][0]
        ny = c + move[dir][1]
        # 범위 안이고 방문 안했으면 추가
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in cafe:
            # 방문 추가하고 재귀
            cafe.append(arr[nx][ny])
            tour(si, sj, nx, ny, dir)
            # 갔던곳 취소하고 방향전환
            cafe.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    # 이동순서
    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    # 방향
    dir = 0
    # 사각형 만들어야 되므로 범위 제한
    for i in range(N-2):
        for j in range(1, N-1):
            # 방문한 카페 리스트
            cafe = []
            cafe.append(arr[i][j])
            tour(i, j, i, j, dir)

    print(f'#{tc} {ans}')