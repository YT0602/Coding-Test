def DFS(n, tst, ci, cj):
    if n == 7:
        s.add(tst)      # 중복제거
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 범위 안이라면 숫자 뒤에 붙이면서 재귀 호출
            DFS(n+1, tst*10 + arr[ni][nj], ni, nj)


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    s = set()

    for i in range(4):
        for j in range(4):
            DFS(1, arr[i][j], i, j)
    ans = len(s)

    print(f'#{tc} {ans}')
