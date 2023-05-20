from collections import deque


def BFS():
    q = deque()
    q.append((r, c))
    arr[r][c] = 1

    while q:
        ci, cj = q.popleft()

        for i in range(8):
            ni, nj = ci + move[i][0], cj + move[i][1]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    q.append((ni, nj))
                    arr[ni][nj] = arr[ci][cj] + 1
                    if ni == target_r and nj == target_c:
                        return arr[ni][nj]-1


T = int(input())
for tc in range(T):
    N = int(input())
    r, c = map(int, input().split())
    target_r, target_c = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    move = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

    ans = BFS()
    if ans:
        print(ans)
    else:
        print(0)
