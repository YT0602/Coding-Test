import sys
input = sys.stdin.readline
from collections import deque


def hunt(r, c, size):
    global cnt
    catch = 0
    q.append((r, c))

    v = [[0] * N for _ in range(N)]
    v[r][c] = 1
    while q:
        si, sj = q.popleft()
        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]
            # 범위 안에 있고 사이즈 이하면 이동
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] <= size:
                    if v[ni][nj] == 0:
                        # 이동거리 표시
                        v[ni][nj] = v[si][sj] + 1
                        q.append((ni, nj))
                        # 이동 위치가 0이 아니고 사이즈보다 작으면 이동해서 잡아먹음
                        if arr[ni][nj] != 0 and arr[ni][nj] < size:
                            catch += 1
                            # 이동시간 추가
                            cnt += v[ni][nj]-1
                            # 잡아먹어서 물고기 사라짐
                            arr[ni][nj] = 0
                            # 잡아먹은 수가 사이즈만큼이면 성장
                            if catch == size:
                                size += 1
                                catch = 0
                            # 이동위치에서 새로 시작
                            q.clear()
                            mn_dis = v[ni][nj]
                            DFS(ni, nj, 0)
                            v = [[0] * N for _ in range(N)]
                            v[ni][nj] = 1
                            break


def DFS(r, c, dis):
    # if dis >
    for k in range(4):
        ni = r + dx[k]
        nj = c + dy[k]
        # 범위 안에 있고 사이즈 이하면 이동
        # if 0 <= ni < N and 0 <= nj < N:


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            hunt(i, j, 2)
print(cnt)
