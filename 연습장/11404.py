import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
# 거리 리스트
INF = int(1e9)
dis = [[INF] * (n+1) for _ in range(n+1)]
# 2차원 배열로 정리
for i in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = min(c, dis[a][b])

# 출발, 도착 같으면 0
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            dis[i][j] = 0


for i in range(1, n+1):  # 중간지점
    for j in range(1, n+1):  # 출발지점
        for k in range(1, n+1):  # 끝지점
            dis[j][k] = min(dis[j][k], dis[j][i]+dis[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == INF:
            dis[i][j] = 0

for i in range(1, n+1):
    print(*dis[i][1:])



