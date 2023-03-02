import heapq
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
# 시작 번호
K = int(input())
# 연결된 노드
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
# 거리 리스트
INF = int(1e9)
dis = [INF] * (V+1)


def daik(start):
    q = []
    # 시작 번호 추가하고 방문표시
    heapq.heappush(q, (0, K))
    dis[K] = 0
    while q:
        x, now = heapq.heappop(q)
        # 이미 방문했다면 건너뜀
        if dis[now] < x:
            continue
        for j in graph[now]:
            # 최단거리 갱신
            cost = x + j[1]
            if cost < dis[j[0]]:
                dis[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


daik(K)
for i in dis[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)