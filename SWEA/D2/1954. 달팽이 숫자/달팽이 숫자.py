T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 0 right, 1 down, 2 left, 3 up
    dx = [0, 1, 0, -1]  # 행
    dy = [1, 0, -1, 0]  # 열
    road = 0
    row = col = 0
    for num in range(1, N**2 + 1):
        arr[row][col] = num
        row += dx[road]
        col += dy[road]
        # 범위 넘어가거나 이미 값이 있으면 되돌리고 방향 전환
        if row < -1 or col < -1 or row >= N or col >= N or arr[row][col] != 0:
            row -= dx[road]
            col -= dy[road]
            # 계속 커지는거 방지
            road = (road + 1) % 4

            row += dx[road]
            col += dy[road]

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])