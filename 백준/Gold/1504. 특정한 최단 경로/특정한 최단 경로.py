import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
inf = int(1e9)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(startnode, target):
    dist = [inf for i in range(n + 1)]
    dist[startnode] = 0
    que = []
    heapq.heappush(que, (dist[startnode], startnode))

    while que:
        cost, node = heapq.heappop(que)

        if dist[node] < cost:
            continue
        for newnode, newcost in graph[node]:
            temp = newcost + cost
            if temp < dist[newnode]:
                dist[newnode] = temp
                heapq.heappush(que, (temp, newnode))

    return dist[target]

a = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
b = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if a >= inf and b >= inf:
    print(-1)
else:
    print(min(a, b))