def check(r, c):
    global cnt
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = r + dx, c + dy
        if 0 <= nx < 100 and 0 <= ny < 100:
            if arr[nx][ny] == 0:
                cnt += 1
        else:
            cnt += 1


N = int(input())
cnt = 0
arr = [[0] * 100 for _ in range(100)]
for i in range(N):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for k in range(x, x+10):
            arr[j][k] += 1
for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            check(i, j)

print(cnt)


