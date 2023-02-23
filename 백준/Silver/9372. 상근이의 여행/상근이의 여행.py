from collections import deque
import sys
input  = sys.stdin.readline


def BFS(n):
    global cnt
    Q.append(n)
    while Q:
        x = Q.popleft()
        for j in graph[x]:
            if visited[j] == 0:
                visited[j] = 1
                Q.append(j)
                cnt += 1
                if sum(visited) == N:
                    return cnt


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    Q = deque()
    visited = [0] * (N + 1)
    cnt = 0
    ans = []
    # for i in range(N):
    #     visited = [0] * (N + 1)
    #     ans.append(BFS(i))
    print(BFS(1)-1)