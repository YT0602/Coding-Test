import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
nodes = [list(map(int, input().split())) for _ in range(N-1)]
graph = [[] for _ in range(N+1)]

# 트리 그래프
for i in range(N-1):
    graph[nodes[i][0]].append((nodes[i][1], nodes[i][2]))
    graph[nodes[i][1]].append((nodes[i][0], nodes[i][2]))
# print(graph)

# 가장 먼 노드 찾기
def DFS(n, road):
    for node, x in graph[n]:
        if dis[node] == -1:
            dis[node] = road + x
            DFS(node, dis[node])

# 1번 노드에서 각 노드 까지의 거리
dis = [-1] * (N+1)
dis[1] = 0
DFS(1, 0)

# 1번에서 가장 먼 노드 번호
start = dis.index(max(dis))
# 가장 먼 노드에서 가장 먼 노드 찾기
dis = [-1] * (N+1)
dis[start] = 0
DFS(start, 0)

print(max(dis))