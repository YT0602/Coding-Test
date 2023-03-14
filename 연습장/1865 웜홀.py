import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M, W = map(int, input().split())
    graph = []
    # 도로연결 (양방향)
    for i in range(M):
        S, E, T = map(int, input().split())
        graph.append([S, E, T])
        graph.append([E, S, T])
    # 웜홀 연결 (단방향)
    for i in range(W):
        S, E, T = map(int, input().split())
        graph.append([S, E, -T])
    # 노드 간 거리
    INF = 1e9
    dis = [INF] * (N+1)


    def wormhole(num):
        dis[num] = 0
        for j in range(N):
            for k in range(len(graph)):
                cur, next, road = graph[k]
                # 최단경로 갱신
                if dis[cur] + road < dis[next]:
                    dis[next] = dis[cur] + road
                    # N-1 일때도 최단경로가 갱신되면 음의 순환 있음
                    if j == N-1:
                        return True
        return False


    if wormhole(1):
        print('YES')
    else:
        print('NO')
    # print(graph)

