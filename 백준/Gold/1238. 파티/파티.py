import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for i in range(M):
    s, e, time = map(int, input().split())
    graph[s].append([e, time])


def daik(num):
    q = []
    dis = [INF] * (N+1)
    heapq.heappush(q, (0, num))
    dis[num] = 0

    while q:
        D, cur = heapq.heappop(q)

        if dis[cur] < D:
            continue
        for node, new_dis in graph[cur]:
            cost = D + new_dis
            if dis[node] > cost:
                dis[node] = cost
                heapq.heappush(q, (cost, node))
    return dis


ans = 0
for i in range(1, N+1):
    go = daik(i)
    back = daik(X)
    ans = max(ans, go[X] + back[i])

print(ans)