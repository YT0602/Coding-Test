from collections import deque

def BFS(num):
    Q.append(num)
    while Q:
        current = Q.popleft()
        for node in graph[current]:
            if visited[node] == 0:
                Q.append(node)
                visited[node] = visited[current] + 1


for tc in range(1, 11):
    num, S = map(int, input().split())
    contact = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    Q = deque()
    visited = [0] * 101

    for i in range(0, num, 2):
        if contact[i+1] not in graph[contact[i]]:
            graph[contact[i]].append(contact[i+1])
    BFS(S)

    mx = max(visited)
    mx_idx = 0

    for idx in range(100, 0, -1):
        if visited[idx] == mx:
            mx_idx = idx
            break

    print(f'#{tc} {mx_idx}')
