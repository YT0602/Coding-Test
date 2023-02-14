import sys
input = sys.stdin.readline

def DFS(arr, num):
    stack.append(num)
    while stack:
        current = stack.pop()
        visited[current] = 1
        for j in arr[current]:
            if visited[j] == 0:
                stack.append(j)


N = int(input())
line = int(input())
graph = [[] for _ in range(N+1)]
stack = []
visited = [0 for _ in range(N+1)]
for i in range(line):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
DFS(graph, 1)
print(sum(visited[1:])-1)