import sys

input = sys.stdin.readline
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
cnt = [0] * (N + 1)
num = N
points = []
for i in range(N):
    square = list(map(int, input().split()))
    points.append(square)
    # x, y, w, h
for i in range(len(points) - 1, -1, -1):
    for j in range(points[i][1], points[i][1] + points[i][3]):
        for k in range(points[i][0], points[i][0] + points[i][2]):
            if arr[j][k] == 0:
                arr[j][k] = num
                cnt[num] += 1
    num -= 1

for i in range(1, N + 1):
    print(cnt[i])