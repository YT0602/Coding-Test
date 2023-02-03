T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    cnt = 0  # 연속된 1 갯수
    max_cnt = 0  # 최대 1 연속 갯수
    for i in numbers:
        if i == 1:
            cnt += 1
            if max_cnt < cnt:  # 최대 횟수가 현재 cnt보다 작으면 갱신
                max_cnt = cnt
        if i == 0:
            cnt = 0
    print(f'#{tc} {max_cnt}')