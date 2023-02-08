import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for i in range(M):
    # 각 노드의 인덱스에 해당 노드와 연결된 노드로 정리
    # 작은 번호 먼저 방문해야 하므로 오름차순 정렬
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[x].sort()
    arr[y].append(x)
    arr[y].sort()


def DFS(graph, v, visited):
    # 현재노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드 재귀로 방문
    for j in graph[v]:
        if not visited[j]:
            DFS(graph, j, visited)


def BFS(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        # 덱에서 맨 앞의 원소 뽑아서 출력
        v = q.popleft()
        print(v, end=' ')
        # 뽑은 원소와 연결된 노드 중에
        for k in graph[v]:
            # 방문하지 않은 원소는 큐에 삽입하고 방문처리
            if not visited[k]:
                q.append(k)
                visited[k] = True


check = [False] * (N+1)
DFS(arr, V, check)
print()
check = [False] * (N+1)
BFS(arr, V, check)