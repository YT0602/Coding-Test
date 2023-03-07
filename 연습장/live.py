T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for si in range(N):
        for sj in range(N):
            # 처음 본인자리 더하기
            cnt = arr[si][sj]
            # 사방탐색
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # 스프레이 거리만큼 곱하기
                for mul in range(1, M):
                    ni, nj = si+di*mul, sj+dj*mul
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            ans = max(ans, cnt)

            cnt = arr[si][sj]
            # x자 탐색
            for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                # 스프레이 거리만큼 곱하기
                for mul in range(1, M):
                    ni, nj = si+di*mul, sj+dj*mul
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            # 최대값 갱신
            ans = max(ans, cnt)

    print(f'#{tc} {ans}')
