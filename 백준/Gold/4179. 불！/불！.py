from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
fire_v = [[0] * C for _ in range(R)]
jihun_v = [[0] * C for _ in range(R)]
jihun = deque()
fire = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            jihun.append((i, j))
        elif arr[i][j] == 'F':
            fire.append((i, j))
            fire_v[i][j] = 1
move = ((-1, 0), (1, 0), (0, -1), (0, 1))


def maze():
    while fire:
        ci, cj = fire.popleft()
        for i in range(4):
            ni, nj = ci + move[i][0], cj + move[i][1]

            if 0 <= ni < R and 0 <= nj < C:
                if not fire_v[ni][nj] and arr[ni][nj] != '#':
                    fire_v[ni][nj] = fire_v[ci][cj] + 1
                    fire.append((ni, nj))

    while jihun:
        ci, cj = jihun.popleft()
        for i in range(4):
            ni, nj = ci + move[i][0], cj + move[i][1]

            if 0 <= ni < R and 0 <= nj < C:
                if not jihun_v[ni][nj] and arr[ni][nj] != '#':
                    if not fire_v[ni][nj] or fire_v[ni][nj] > jihun_v[ci][cj] + 2:
                        jihun_v[ni][nj] = jihun_v[ci][cj] + 1
                        jihun.append((ni, nj))
            else:
                return jihun_v[ci][cj] + 1
    return 'IMPOSSIBLE'


print(maze())

