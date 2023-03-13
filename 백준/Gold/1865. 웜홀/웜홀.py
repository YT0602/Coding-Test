import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M, W = map(int, input().split())
    graph = []
    for i in range(M):
        S, E, T = map(int, input().split())
        graph.append([S, E, T])
        graph.append([E, S, T])
    for i in range(W):
        S, E, T = map(int, input().split())
        graph.append([S, E, -T])
    INF = 1e9
    dis = [INF] * (N+1)


    def wormhole(num):
        dis[num] = 0
        for j in range(N):
            for k in range(len(graph)):
                cur, next, road = graph[k]
                if dis[cur] + road < dis[next]:
                    dis[next] = dis[cur] + road
                    if j == N-1:
                        return True
        return False


    if wormhole(1):
        print('YES')
    else:
        print('NO')
    # print(graph)

