import heapq


N, M = map(int, input().split())
# 그래프
graph = [[] for _ in range(N+1)]
# 진입차수
in_node = [0] * (N+1)
q = []
result = []

for i in range(M):
    start, end = map(int, input().split())
    in_node[end] += 1
    graph[start].append(end)

for i in range(1, N+1):
    if in_node[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    result.append(cur)
    for nxt in graph[cur]:
        in_node[nxt] -= 1
        if in_node[nxt] == 0:
            heapq.heappush(q, nxt)

print(*result)
