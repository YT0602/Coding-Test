def DFS(r, c):
    global cnt
    for k in range(4):
        nx = r + dx[k]
        ny = c + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            # 방 번호가 1 크면 이동
            if room[nx][ny] - room[r][c] == 1:
                cnt += 1
                visited[nx][ny] = 1
                DFS(nx, ny)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    mx_cnt = 1
    room_num = N**2

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt = 1
                DFS(i, j)
                # 최대 방 탐색 수 갱신
                if cnt > mx_cnt:
                    mx_cnt = cnt
                    room_num = room[i][j]
                # 같다면 방 번호 갱신
                elif cnt == mx_cnt:
                    room_num = min(room_num, room[i][j])
    print(f'#{tc} {room_num} {mx_cnt}')
