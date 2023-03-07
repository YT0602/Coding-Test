import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
# 연결된 도시 리스트
bus = [[] for _ in range(N+1)]
for i in range(M):
    A, B, dis = map(int, input().split())
    bus[A].append([B, dis])

S, E = map(int, input().split())
INF = int(1e9)
# 각 도시까지 가는 비용 리스트
road = [INF] * (N+1)


def daik(S):
    q = []
    # 시작 도시 추가
    heapq.heappush(q, (0, S))
    # 방문표시
    road[S] = 0
    while q:
        x, now = heapq.heappop(q)
        # 꺼낸 도시까지 최소 비용이 이미 더 작다면 방문했다는 의미이므로 건너뜀
        if road[now] < x:
            continue
        for j in bus[now]:
            # 비용 = 현재 도시까지 비용 + 현재 도시에서 다음도시까지 비용
            cost = j[1] + x
            # 더 작다면 갱신하고 push
            if cost < road[j[0]]:
                road[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


daik(S)
print(road[E])


