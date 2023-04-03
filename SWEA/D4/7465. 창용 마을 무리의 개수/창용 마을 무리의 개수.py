def DFS(num):
    for j in graph[num]:
        if not v[j]:
            v[j] = True
            DFS(j)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    ans = 0
    v = [False] * (N+1)

    for i in range(1, N+1):
        if not v[i]:
            v[i] = True
            DFS(i)
            ans += 1
    print(f'#{tc} {ans}')