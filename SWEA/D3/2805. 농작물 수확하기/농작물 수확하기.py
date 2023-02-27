T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    x = 0
    cnt = 0

    for i in range(N):
        for j in range(N//2-x, N//2+x+1):
            cnt += arr[i][j]
        if i < N//2:
            x += 1
        else:
            x -= 1

    print(f'#{tc} {cnt}')