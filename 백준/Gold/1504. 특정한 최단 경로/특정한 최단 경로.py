import sys
import heapq
inpuy = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 그래프 연결
for i in range(E):
    S, E, dis = map(int, input().split())
    graph[S].append([E, dis])
    graph[E].append([S, dis])
x, y = map(int, input().split())
INF = int(1e9)


def daik(num):
    road = [INF] * (N + 1)
    q = []
    # 시작 배열 추가하고 거리 0
    heapq.heappush(q, (0, num))
    road[num] = 0

    while q:
        dis, cur = heapq.heappop(q)
        # 방문했었다면 건너뜀
        if road[cur] < dis:
            continue
        for j in graph[cur]:
            # 최단거리 갱신
            new = dis + j[1]
            if new < road[j[0]]:
                road[j[0]] = new
                heapq.heappush(q, (new, j[0]))
    return road


node1 = daik(1)
node_x = daik(x)
node_y = daik(y)
# 1 - x - y - N, 1 - y - x - N 중에 작은 값
ans = min(node1[x] + node_x[y] + node_y[N], node1[y] + node_y[x] + node_x[N])

if ans < INF:
    print(ans)
else:
    print(-1)