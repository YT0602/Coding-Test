from itertools import combinations
import copy
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최솟값
mn_cnt = 9999
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 치킨집 좌표 추가
ck = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            # 전체 치킨집 좌표 리스트
            ck.append([i, j])


def BFS():
    global cnt
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 길이면 방문처리하고 거리표시
                if tmp[nx][ny] == 0:
                    v[nx][ny] = v[cx][cy] + 1
                    tmp[nx][ny] = 9
                    q.append([nx, ny])
                # 집이면 방문처리하고 거리추가
                if tmp[nx][ny] == 1:
                    v[nx][ny] = v[cx][cy] + 1
                    cnt += v[nx][ny]
                    tmp[nx][ny] = 9
                    q.append([nx, ny])


# 폐업할 치킨집 있는 경우
if len(ck) > M:
    # 폐업할 치킨 집 고르는 경우의 수
    for close in combinations(ck, len(ck) - M):
        # 테스트용 배열 복사
        tmp = copy.deepcopy(arr)
        q = copy.deepcopy(ck)
        # 거리 배열
        v = [[0] * N for _ in range(N)]
        # 치킨집 리스트에서 폐업한 곳 삭제
        for x, y in close:
            tmp[x][y] = 0
            q.remove([x, y])
        # BFS 후 최솟값 갱신
        cnt = 0
        BFS()
        mn_cnt = min(cnt, mn_cnt)
# 폐업 안해도 됨
else:
    # 테스트용 배열 복사
    tmp = copy.deepcopy(arr)
    q = copy.deepcopy(ck)
    # 거리 배열
    v = [[0] * N for _ in range(N)]
    cnt = 0
    BFS()
    mn_cnt = min(cnt, mn_cnt)

print(mn_cnt)