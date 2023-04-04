"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
# def DFS(num):
#     for i in graph[num]:
#         if not v[i]:
#             v[i] = True
#             print(i, end=' ')
#             DFS(i)
#
#
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))
# graph = [[] for _ in range(N+1)]
# for i in range(0, len(numbers)-1, 2):
#     graph[numbers[i]].append(numbers[i+1])
#
# v = [False] * (N+1)
# print(1, end=' ')
# DFS(1)
# print()
# print(graph)

n = dict()
num = [1,1,2,3,4,5]
for i in num:
    n.setdefault()
    # n[i] += 1
print(n)
new = sorted(n, key=lambda x: x)