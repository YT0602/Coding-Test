T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    di, dj = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
    # 반대방향 테이블
    tbl = [0, 2, 1, 4, 3]

    ans = 0

    for _ in range(M):
        # 1칸 이동처리, 경계면이면 N // 2, 방향 반대
        for i in range(len(arr)):
            # [0] : r, [1] : c, [2] : n, [3] : dir
            # ni = ci + di[dir], nj = cj + dj[dir]
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            # 가장자리면 절반되고 방향반대
            if arr[i][0] == N-1 or arr[i][1] == N-1 or arr[i][0] == 0 or arr[i][1] == 0:
                arr[i][2] //= 2
                arr[i][3] = tbl[arr[i][3]]
        # 내림차순 정렬
        # 이동 좌표가 같은 경우 미생물 수가 많은 순서로 정렬
        arr.sort(key=lambda x: [x[0], x[1], x[2]], reverse=True)
        # 같은좌표 합치기
        i = 1
        while i < len(arr):
            # 위의 미생물이랑 좌표같으면 합치고 제거
            if arr[i-1][0:2] == arr[i][0:2]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1

    for lst in arr:
        ans += lst[2]

    print(f'#{tc} {ans}')
