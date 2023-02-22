import sys
from collections import deque
input = sys.stdin.readline

def BFS(num):
    Q.append(num)
    while Q:
        x = Q.popleft()
        for j in graph[x]:
            if visited[j] == 0:
                Q.append(j)
                visited[j] = x


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    S, E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)
Q = deque()
visited = [0] * (N+1)
BFS(1)
for i in visited[2:]:
    print(i)