import heapq
import sys
input = sys.stdin.readline


N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
# 기본거리 !!
for i in range(D):
    graph[i].append([i+1, 1])
# 지름길 있는 경우
for i in range(N):
    s, e, dis = map(int, input().split())
    # 목적지 벗어나는건 건너뜀 !!
    if e > D:
        continue
    graph[s].append([e, dis])

v = [10000] * (D+1)


def daik(num):
    q = []
    heapq.heappush(q, [0, num])
    v[num] = 0
    # 다익스트라
    while q:
        cost, cur = heapq.heappop(q)
        if v[cur] < cost:
            continue
        for node, new_dis in graph[cur]:
            new = new_dis + cost
            if new < v[node]:
                v[node] = new
                heapq.heappush(q, [new, node])


daik(0)
print(v[-1])