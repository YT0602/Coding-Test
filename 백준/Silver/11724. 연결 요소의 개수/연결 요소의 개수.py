import sys
input = sys.stdin.readline

def DFS(arr, num):
    stack.append(num)
    while stack:
        current = stack.pop()
        visited[current] = 1
        for i in arr[current]:
            if visited[i] == 0:
                stack.append(i)


node, line = map(int, input().split())
graph = [[] for _ in range(node + 1)]
cnt = 0
stack = []
visited = [0 for _ in range(node + 1)]
for i in range(line):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for j in range(1, node + 1):
    if visited[j] == 0:
        cnt += 1
        DFS(graph, j)
    if sum(visited[1:]) == node:
        break

print(cnt)