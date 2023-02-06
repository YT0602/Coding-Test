T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    dx = [1, -1, 0, 0]  # 행 이동
    dy = [0, 0, 1, -1]  # 열 이동
    max_cnt = 0
    for j in range(N):
        for k in range(M):
            cnt = 0
            cnt += arr[j][k]  # 현재 좌표 꽃가루 추가
            for l in range(4):
                if 0 <= j + dx[l] < N and 0 <= k + dy[l] < M:  # 이동한 좌표가 배열 안이면 해당 꽃가루 추가
                    cnt += arr[j+dx[l]][k+dy[l]]
            if cnt > max_cnt:  # 최대 꽃가루보다 크면 갱신
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')