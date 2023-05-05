from collections import deque

tc = int(input())
for _ in range(tc):
    N = int(input())

    graph = [[] for _ in range(N+1)]
    in_node = [0] * (N+1)
    q = deque()
    new_rank = []

    rank = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(i+1, N):
            graph[rank[i]].append(rank[j])
            in_node[rank[j]] += 1

    M = int(input())
    for _ in range(M):
        first, second = map(int, input().split())
        if first in graph[second]:
            # 간선 제거하고 진입차수 -1
            graph[second].remove(first)
            in_node[first] -= 1
            # 간선 새로 추가하고 진입차수 + 1
            graph[first].append(second)
            in_node[second] += 1
        else:
            graph[first].remove(second)
            in_node[second] -= 1
            graph[second].append(first)
            in_node[first] += 1

    # 진입차수 0인 노드 큐에 삽입
    for i in range(1, N+1):
        if in_node[i] == 0:
            q.append(i)

    ans = True
    while q:
        # 처음에 진입차수가 0인 노드가 2개이상 있으면 불가능
        if len(q) > 1:
            ans = False
            break

        cur = q.popleft()
        new_rank.append(cur)
        for j in graph[cur]:
            in_node[j] -= 1
            if in_node[j] == 0:
                q.append(j)
            elif in_node[j] < 0:
                ans = False
                break
    if not ans or len(new_rank) < N:
        print("IMPOSSIBLE")
    else:
        print(*new_rank)
    # print(graph)
