import sys

input = sys.stdin.readline
N = int(input())
arr = [[0]*1001 for _ in range(1001)]
num = 1
cnt = [0] * (N + 1)
for i in range(N):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        for k in range(x, x+w):
            arr[j][k] = num
    num += 1
for i in arr:
    for j in range(1, num):
        cnt[j] += i.count(j)
for i in range(1, N+1):
    print(cnt[i])