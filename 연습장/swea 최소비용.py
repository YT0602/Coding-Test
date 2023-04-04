import heapq


def daik():
    q = [(0, 0, 0)]
    dis[0][0] = 0

    while q:
        cost, ci, cj = heapq.heappop(q)
        if dis[ci][cj] < cost:
            continue
        for ni, nj, road in graph[ci][cj]:
            # 높이가 낮은경우 0으로 설정
            if road < 0:
                road = 0
            # 기본거리 1 더해주기
            new = road + dis[ci][cj] + 1
            if new < dis[ni][nj]:
                dis[ni][nj] = new
                heapq.heappush(q, (dis[ni][nj], ni, nj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [[[] for _ in range(N)] for _ in range(N)]
    INF = 1e9
    # 거리 저장 리스트
    dis = [[INF] * N for _ in range(N)]
    move = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for i in range(N):
        for j in range(N):
            # 인접 리스트 만들기
            for k in range(4):
                ni = i + move[k][0]
                nj = j + move[k][1]
                if 0 <= ni < N and 0 <= nj < N:
                    graph[i][j].append((ni, nj, arr[ni][nj]-arr[i][j]))


    daik()
    print(f'#{tc} {dis[N-1][N-1]}')