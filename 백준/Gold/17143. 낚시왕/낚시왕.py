import sys
input = sys.stdin.readline

from collections import deque

R, C, M = map(int, input().split())
arr = [[0] * C for _ in range(R)]
q = deque()
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = [s, d-1, z]

move = ((-1, 0), (1, 0), (0, 1), (0, -1))
ch_dir = {0:1, 1:0, 2:3, 3:2}
ans = 0


# 낚시
def fishing(n):
    global ans
    for i in range(R):
        if arr[i][n] != 0:
            ans += arr[i][n][-1]
            arr[i][n] = 0
            break


# 상어이동
def shark(arr):
    tmp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if arr[x][y] != 0:
                r, c, s, d, z = x, y, arr[x][y][0], arr[x][y][1], arr[x][y][2]
                for i in range(s):
                    r += move[d][0]
                    c += move[d][1]
                    # 범위 벗어나면 방향 전환
                    if r < 0 or r >= R or c < 0 or c >= C:
                        r -= move[d][0]
                        c -= move[d][1]
                        d = ch_dir[d]
                        r += move[d][0]
                        c += move[d][1]
                if tmp[r][c] != 0:
                    if tmp[r][c][-1] < z:
                        tmp[r][c] = [s, d, z]
                else:
                    tmp[r][c] = [s, d, z]

    return tmp


for i in range(C):
    fishing(i)
    arr = shark(arr)
print(ans)
