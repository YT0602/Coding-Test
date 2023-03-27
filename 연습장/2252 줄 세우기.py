import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
road = []
rank = deque()
num_list = []
v = [0] * (N+1)
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    num_list.append(s)



def DFS(num):
    v[num] = 1
    road.append(num)
    for k in graph[num]:
        if v[k] == 0:
            v[k] = 1
            DFS(k)
            rank.appendleft(road.pop())


for i in num_list:
    DFS(i)
    rank.appendleft(road.pop())

print(*rank)
# print(v)
# print(graph)