from collections import deque


def BFS():
    cnt = 0
    for i in range(1, N+1):
        if not v[i]:
            q = deque([i])
            v[i] = True
            cnt += 1
        while q:
            cur = q.popleft()
            for j in graph[cur]:
                if not v[j]:
                    v[j] = True
                    q.append(j)

    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    v = [False] * (N+1)

    ans = BFS()
    print(f'#{tc} {ans}')

