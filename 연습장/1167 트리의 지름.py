import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

V = int(input())
# 트리 리스트
graph = [[] for _ in range(V+1)]
# 노드 담을 리스트
q = deque()
# 방문 리스트
v = [-1] * (V+1)
# 최대 거리
mx_dis = 0


# 연결된 노드와 거리 추가
for i in range(V):
    numbers = list(map(int, input().split()))
    for j in range(1, len(numbers), 2):
        if numbers[j] == -1:
            break
        else:
            graph[numbers[0]].append((numbers[j], numbers[j+1]))


# DFS로 가장 먼 노드 탐색
def tree(num, dis):
    # 방문하지 않았으면 방문처리하고 재귀 호출
    for next, tmp in graph[num]:
        if v[next] == -1:
            v[next] = 0
            v[next] += v[num] + tmp
            tree(next, tmp)


# 루트노드 방문처리하고 가장 먼 노드 찾기
v[1] = 0
tree(1, 0)

# 루트노드에서 가장 먼 노드
target = v.index(max(v))

# 방문 초기화
v = [-1] * (V+1)

# 가장 먼 노드에서 가장 먼 노드 찾기
v[target] = 0
tree(target, 0)
print(max(v))
