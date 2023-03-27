import sys
input = sys.stdin.readline
from collections import deque
# 위상정렬
"""
1. 진입차수가 0인 정점을 큐에 삽입
2. 큐에서 원소 꺼내 해당 원소와 연결된 간선 모두 제거
3. 제거한 후에 진입차수 0인 정점 큐에 삽입
반복
"""
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
rank = deque()
ans = []
v = [0] * (N+1)

for i in range(M):
    s, e = map(int, input().split())
    # 연결된 노드
    graph[s].append(e)
    # 진입차수 추가
    v[e] += 1

# 1. 진입차수 0인 정점 큐에 삽입
for i in range(1, N+1):
    if v[i] == 0:
        rank.append(i)

# 2. 큐에서 원소 꺼내 해당 원소와 연결된 간선 모두 제거
while rank:
    cur = rank.popleft()
    ans.append(cur)

    for j in graph[cur]:
        v[j] -= 1

        # 3. 제거한 후에 진입차수 0이면 큐에 삽입
        if v[j] == 0:
            rank.append(j)

print(*ans)