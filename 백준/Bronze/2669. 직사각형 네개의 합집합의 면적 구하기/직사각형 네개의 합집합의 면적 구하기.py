import sys

input = sys.stdin.readline
arr = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for j in range(y1, y2):
        for k in range(x1, x2):
            if arr[j][k] == 0:
                arr[j][k] += 1
for i in range(100):
    cnt += sum(arr[i])
print(cnt)