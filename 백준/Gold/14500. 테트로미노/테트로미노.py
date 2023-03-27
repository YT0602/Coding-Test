import sys

input = sys.stdin.readline


def DFS(r, c, idx, cnt):
    global mx_cnt
    # 남은 칸들이 배열의 최댓값이더라도 최댓값보다 작으면 탐색 종료
    if mx_cnt >= cnt + max_val * (3 - idx):
        return
    # 깊이 3까지 왔다면 최댓값 갱신
    if idx == 3:
        mx_cnt = max(mx_cnt, cnt)
        return
    else:
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc] == 0:
                    # ㅗ 모양 탐색
                    if idx == 1:
                        visit[nr][nc] = 1
                        DFS(r, c, idx + 1, cnt + arr[nr][nc])
                        visit[nr][nc] = 0
                    # 다른 모양 탐색
                    visit[nr][nc] = 1
                    DFS(nr, nc, idx + 1, cnt + arr[nr][nc])
                    visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mx_cnt = 0
# 배열 안의 값 중 최댓값
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        # 탐색 후 방문처리 해제
        visit[r][c] = 1
        DFS(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(mx_cnt)