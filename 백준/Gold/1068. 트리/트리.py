import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())  # 삭제할 노드 번호
par = [[] for _ in range(N)]  # 각 노드별 자식 노드 번호
leaf = deque()  # 삭제노드의 자식노드
ans = []  # 리프노드 번호

for i in range(N):
    if nodes[i] == -1:
        continue
    else:
        par[nodes[i]].append(i)

# 리프노드 체크
for i in range(N):
    if del_node in par[i]:
        par[i].remove(del_node)
    if len(par[i]) == 0:
        ans.append(i)


# 삭제노드에 리프노드있으면 제거
if len(par[del_node]) != 0:
    for i in par[del_node]:
        leaf.append(i)
        if i in ans:
            ans.remove(i)
else:
    ans.remove(del_node)

while leaf:
    del_node = leaf.popleft()
    if par[del_node] != 0:
        for i in par[del_node]:
            leaf.append(i)
            if i in ans:
                ans.remove(i)

print(len(ans))