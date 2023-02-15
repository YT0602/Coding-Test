def DFS(arr, x):
    stack.append(x)
    while stack:
        current = stack.pop()
        visited.append(current)
        for j in arr[current]:
            if j not in visited:
                stack.append(j)


for tc in range(1, 11):
    T, num = map(int, input().split())
    line = list(map(int, input().split()))
    node = []
    graph = [[] for _ in range(100)]
    stack = []
    visited = []
    ans = 1
    for i in range(0, 2*num, 2):
        node.append((line[i], line[i+1]))
    for i in node:
        graph[i[0]].append(i[1])
    DFS(graph, 0)
    if 99 not in visited:
        ans = 0
    # print(graph)
    print(f'#{tc} {ans}')