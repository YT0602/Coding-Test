N, M = map(int, input().split())
graph = []
# 처음 부모는 자기자신
parent = [i for i in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    graph.append((cost, s, e))

graph.sort()


# 부모 찾기
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


# 노드 번호 큰 쪽의 부모노드를 연결된 노드의 부모 노드로 지정
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0  # 연결된 마을 간의 비용
last = 0  # 가장 유지비가 큰 마을 비용

for i in range(M):
    cost, s, e = graph[i]

    # 연결된 노드의 부모노드가 다르면 사이클이 없으므로
    # union 수행하고 최소 신장 트리에 포함
    if find_parent(s) != find_parent(e):
        union(s, e)
        ans += cost
        last = cost
    
print(ans - last)
