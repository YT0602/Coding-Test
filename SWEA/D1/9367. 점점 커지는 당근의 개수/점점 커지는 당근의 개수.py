T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    cnt = 1  # 연속 당근
    max_cnt = 1  # 최대 연속 당근
    for i in range(N - 1):
        if carrots[i + 1] - carrots[i] == 1:  # 크기 차이 1이면 1 증가
            cnt += 1
        else:  # 아니면 cnt 초기화
            cnt = 1
        if max_cnt < cnt:  # 현재 cnt가 최대보다 크면 갱신
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')