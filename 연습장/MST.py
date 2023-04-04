"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
# 노드개수, 간선
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, dis = map(int, input().split())
    graph[u].append([v, dis])


import heapq
# 프림 알고리즘
# 반환값이 MST 모든 가중치 합한 값
def prim(graph):
    v = [False for _ in range(len(graph))]
    q = [(0, 0)]
    total = 0


# 크루스칼 알고리즘