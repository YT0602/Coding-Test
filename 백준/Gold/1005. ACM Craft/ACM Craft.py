from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 건설시간
    build = [0] + list(map(int, input().split()))
    # 간선
    graph = [[] for _ in range(N+1)]
    # 진입차수
    innode = [0] * (N+1)
    # 해당 건물까지 시간
    dp = [0] * (N+1)
    # 노드 연결
    for i in range(K):
        s, e = map(int, input().split())
        graph[s].append(e)
        innode[e] += 1

    target = int(input())
    # 진입차수 0 인 노드 큐에 삽입
    q = deque()
    for i in range(1, N+1):
        if innode[i] == 0:
            q.append(i)
            dp[i] = build[i]
    # 위상정렬 이용
    # 진입차수 1씩 줄이면서 0이되면 큐에 삽입
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            dp[i] = max(dp[cur]+build[i], dp[i])
            innode[i] -= 1
            if innode[i] == 0:
                q.append(i)

    print(dp[target])