import sys

input = sys.stdin.readline

N = int(input())
xy_list = []
for i in range(N):
    x, y = map(int, input().split())
    xy_list.append((x, y))

xy_list.sort(key=lambda x: (x[1], x[0]))  # 1순위 y좌표 기준 정렬 2순위 x좌표 기준정렬
for i in xy_list:
    print(*i)
