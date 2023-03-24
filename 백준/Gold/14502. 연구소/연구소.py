import sys
from collections import deque
import copy
input = sys.stdin.readline
# 벽의 위치 모든 경우의 수를 따져봐야함
# 브루트포스 하면서 BFS 탐색
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
safe = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    # 바이러스 위치 큐에 삽입
    # 벽 위치 바뀔때마다 BFS하므로 함수 안에서 바이러스 위치 큐에 삽입
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append([i, j])

    # 테스트용 배열
    test = copy.deepcopy(arr)
    # 바이러스 확산
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if test[nx][ny] == 0:
                    test[nx][ny] = 2
                    q.append([nx, ny])
    # 안전 영역
    global safe
    cnt = 0
    # 안전영역 카운트 후 갱신
    for j in range(N):
        for k in range(M):
            if test[j][k] == 0:
                cnt += 1
    safe = max(safe, cnt)


# 벽이 3개 세워지면 BFS 시작
def wall(num):
    if num == 3:
        BFS()
        return

    for j in range(N):
        for k in range(M):
            # 백트래킹
            if arr[j][k] == 0:
                arr[j][k] = 1
                wall(num+1)
                arr[j][k] = 0


wall(0)
print(safe)
