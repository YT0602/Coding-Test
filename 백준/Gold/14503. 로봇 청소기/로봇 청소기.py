import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, dir = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 청소한 칸
cnt = 0
arr = [list(map(int, input().split())) for _ in range(N)]


def clean(r, c):
    global cnt
    global dir
    # 현재칸 청소 안했으면 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    # 사방 탐색 중 청소 안된 방 있으면
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if arr[nx][ny] == 0:
            # 일단 방향전환
            dir = (dir - 1) % 4
            # 앞의 칸이 청소 안한 칸일때까지 회전
            while arr[r+dx[dir]][c+dy[dir]] != 0:
                dir = (dir - 1) % 4
            # 재귀 호출
            clean(r+dx[dir], c+dy[dir])
            return
    # 청소 안한 칸이 없다면
    else:
        # 후진 가능하면 후진하고 재귀
        nx = r-dx[dir]
        ny = c-dy[dir]
        if arr[nx][ny] != 1:
            clean(nx, ny)
        # 벽이면 리턴
        else:
            return


clean(r, c)
print(cnt)