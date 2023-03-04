H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

cloud = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            cloud[i][j] = 0
        else:
            if j > 0 and cloud[i][j-1] != -1:
                cloud[i][j] = cloud[i][j-1] + 1
for i in cloud:
    print(*i)
