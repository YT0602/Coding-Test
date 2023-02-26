import sys
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
tour = set()
tour.add(nodes[0])

dp = [0] * 200001
dp[nodes[0]] = -1

for i in range(1, N):
    if nodes[i] not in tour:
        dp[nodes[i]] = nodes[i-1]
        tour.add(nodes[i])


print(len(tour))

for i in range(len(tour)):
    print(dp[i], end=' ')