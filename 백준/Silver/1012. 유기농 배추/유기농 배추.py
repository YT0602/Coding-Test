import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # 상하좌우 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # BFS
    q = deque()
    # 지렁이 수
    cnt = 0
    for j in range(M):
        for k in range(N):
            if arr[k][j] == 1:  # 배열 돌면서 1이면 BFS 실행
                q.append([k, j])  # 해당 좌표 덱이 넣고 0으로 변경
                arr[k][j] = 0
                while q:
                    # 덱에 있는 좌료 꺼내서 인접 원소 탐색
                    a, b = q.popleft()
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        # 배열 범위 벗어나면 건너뜀
                        if nx >= N or nx < 0 or ny >= M or ny < 0:
                            continue
                        # 1이면 덱에 넣고 0으로 변경
                        if arr[nx][ny] == 1:
                            q.append((nx, ny))
                            arr[nx][ny] = 0
                cnt += 1  # 탐색 끝나면 cnt + 1

    print(cnt)