import sys
input = sys.stdin.readline

V, E = map(int, input().split())
# 처음 부모노드는 자기자신
parent = [i for i in range(V+1)]
# 간선 연결
edges = []
for _ in range(E):
    s, e, dis = map(int, input().split())
    edges.append([dis, s, e])

edges.sort()
ans = 0


# 부모노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 노드번호 큰 쪽의 부모노드를 연결된 노드의 부모노드로 지정
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(E):
    dis, s, e = edges[i]
    # 연결된 노드의 부모노드가 다르면 사이클이 없으므로 union 수행하고 최소 신장 트리에 포함
    if find(s) != find(e):
        union(s, e)
        ans += dis


print(ans)