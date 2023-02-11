import sys
input = sys.stdin.readline


C, R = map(int, input().split())  # C: 가로, R: 세로
N = int(input())
arr = [[0]*C for _ in range(R)]
row = R-1
col = 0
road = 1  # 방향
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
if N > C*R:
    print(0)
else:
    for num in range(1, N*R+1):
        arr[row][col] = num
        if num == N:
            print(col + 1, R - row)
            break
        row += dx[road]
        col += dy[road]
        # 범위 넘어가거나 이미 배정됐으면 되돌리고 방향 전환해서 이동
        if row >= R or row < 0 or col >= C or col < 0 or arr[row][col] != 0:
            row -= dx[road]
            col -= dy[road]

            road = (road + 1) % 4
            row += dx[road]
            col += dy[road]