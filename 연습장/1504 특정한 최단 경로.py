import sys
import heapq
inpuy = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    S, E, dis = map(int, input().split())
    graph[S].append([E, dis])
    graph[E].append([S, dis])
x, y = map(int, input().split())

INF = int(1e9)
road = [INF] * (N+1)


def daik(num):
    q = []
    heapq.heappush(q, (0, num))
    road[num] = 0

    while q:
        dis, cur = heapq.heappop(q)
        if road[cur] < dis


print(graph)
print(road)