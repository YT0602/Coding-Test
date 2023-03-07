def solve():
    for si in range(1, N+1):
        for sj in range(1, N+1):
            for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                # 4방향으로 5개까지 탐색
                for mul in range(5):
                    ni, nj = si+di*mul, sj + dj*mul
                    if arr[ni][nj] != 'o':
                        break
                else:
                    return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # . 으로 둘러싸기
    arr = ['.'*(N+2)] + ['.' + input() + '.' for _ in range(N)] + ['.'*(N+2)]

    ans = solve()

    print(f'#{tc} {ans}')
    print(arr)