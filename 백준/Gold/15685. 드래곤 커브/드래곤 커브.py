N = int(input())
arr = [[0] * 101 for _ in range(101)]
move = ((0, 1), (-1, 0), (0, -1), (1, 0))

for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1

    curve = [d]
    for j in range(g):
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    # 드래곤 커브 만들기
    for j in curve:
        y, x = y + move[j][0], x + move[j][1]
        if 0 <= x < 101 and 0 <= y < 101:
            arr[y][x] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i + 1][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j + 1] == 1:
            ans += 1

print(ans)