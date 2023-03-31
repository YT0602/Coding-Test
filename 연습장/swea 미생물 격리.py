from collections import deque


def time(num):
    while num < M:
        micro()
        num += 1


def find_dir(list):
    for a, b in list:
        mx = 0
        sm = 0
        D = 0
        for i, ddir in range(0, len(arr[a][b]), 2):
            if i > mx:
                mx = i
                sm += i
                D = ddir
        arr[a][b] = [sm, D]


def micro():
    cnt = 0
    x = len(q)
    find_list = []
    while q:
        cnt += 1
        if cnt == x:
            break
        ci, cj, now_dir = q.popleft()
        ni, nj = ci + dx[now_dir], cj + dy[now_dir]
        if ni == N-1 or nj == N-1:
            arr[ni][nj] = arr[ci][cj] // 2
            if now_dir == 1:
                q.append([ni, nj, 2])
            elif now_dir == 3:
                q.append([ni, nj, 4])
            else:
                q.append([ni, nj, dir-1])
        else:
            if arr[ni][nj] != 0:
                arr[ni][nj] += arr[ci][cj]
                if [ni, nj] not in find_list:
                    find_list.append([ni, nj])
            else:
                arr[ni][nj] = arr[ci][cj]
            arr[ci][cj] = 0

    find_dir(find_list)


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    q = deque()

    for i in range(K):
        r, c, num, dir = map(int, input().split())
        arr[r][c] = [num, dir-1]
        q.append([r, c, dir-1])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    time(0)

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                ans += arr[i][j]

    print(f'#{tc} {ans}')
    print(arr)
