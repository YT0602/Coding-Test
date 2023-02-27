import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1)]
for i in range(N):
    arr.append([0]+list(map(int, input().split())))

sum_arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_arr[i][j] = sum_arr[i][j-1]+sum_arr[i-1][j] - sum_arr[i-1][j-1]+arr[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1]
    print(ans)