import sys

input = sys.stdin.readline
from collections import deque


def hunt(r, c, size):
    global cnt
    global catch
    q.append((r, c))

    v = [[0] * N for _ in range(N)]
    v[r][c] = 1
    while q:
        si, sj = q.popleft()

        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]
            # 범위 안에 있고 사이즈 이하면 이동
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= size:
                if v[ni][nj] == 0:
                    # 이동거리 표시
                    v[ni][nj] = v[si][sj] + 1
                    if food:
                        if v[ni][nj] > food[-1][-1]:
                            continue
                        else:
                            q.append((ni, nj))
                    else:
                        q.append((ni, nj))

                    # 이동 위치가 0이 아니고 사이즈보다 작으면 이동해서 잡아먹음
                    if arr[ni][nj] != 0 and arr[ni][nj] < size:
                        if food:
                            # 잡아먹을 수 있는 먹이들 보다 멀면 제일 위거나 왼쪽인 먹이로 이동
                            if v[ni][nj] <= food[-1][-1]:
                                food.append((ni, nj, v[ni][nj]))

                        else:
                            food.append((ni, nj, v[ni][nj]))
    if food:
        ni, nj = catch_near()
        catch += 1
        # 이동시간 추가
        cnt += v[ni][nj] - 1
        # 잡아먹어서 물고기 사라짐
        arr[ni][nj] = 0
        # 잡아먹은 수가 사이즈만큼이면 성장
        if catch == size:
            size += 1
            catch = 0
        # 이동위치에서 새로 시작
        q.clear()
        food.clear()
        hunt(ni, nj, size)


def catch_near():
    food.sort(key=lambda x: (x[0], x[1]))
    return food[0][0], food[0][1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
food = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cnt = 0
catch = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            hunt(i, j, 2)
print(cnt)
