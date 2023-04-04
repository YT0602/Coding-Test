from collections import deque

def solution(n, com):
    ans = 0
    for i in com:
        print(i)
    # 방문체크
    v = [False] * (n+1)
    # 인접리스트 연결
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if com[i][j]:
                    graph[i+1].append(j+1)
    print(graph)
    
    def BFS(num):
        q = deque([num])
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if not v[i]:
                    v[i] = True
                    q.append(i)
                    
                    
    for i in range(1, n+1):
        if not v[i]:
            ans += 1
            BFS(i)
    return ans