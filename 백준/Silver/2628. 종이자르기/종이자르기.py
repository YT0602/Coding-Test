import sys
input = sys.stdin.readline

x, y = map(int, input().split())  # 가로, 세로
N = int(input())
box = 0
points_row = [0]
points_col = [0]
for i in range(N):
    point = list(map(int, input().split()))
    if point[0] == 0:
        points_row.append(point[1])
    else:
        points_col.append(point[1])

points_row.sort()
points_col.sort()
points_row.append(y)
points_col.append(x)

for i in range(len(points_col)-1):
    for j in range(len(points_row)-1):
        if (points_col[i+1] - points_col[i]) * (points_row[j+1] - points_row[j]) > box:
            box = (points_col[i+1] - points_col[i]) * (points_row[j+1] - points_row[j])
print(box)
