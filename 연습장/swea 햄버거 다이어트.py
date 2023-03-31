def comb(num, sc_sum, cal_sum, ):
    global mx_sc
    # 칼로리 초과면 반환
    if cal_sum > L:
        return
    # 최대 점수 갱신
    mx_sc = max(mx_sc, sc_sum)
    # 최대점수 계산 후에 반환하기
    if num >= N:
        return
    # 해당 번호 재료 넣는경우, 안넣는경우
    comb(num + 1, sc_sum + burger[num][0], cal_sum + burger[num][1])
    comb(num + 1, sc_sum, cal_sum)


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    burger = []
    mx_sc = 0

    for i in range(N):
        score, cal = map(int, input().split())
        burger.append([score, cal])
    # 재료번호, 점수 합, 칼로리 합
    comb(0, 0, 0)
    print(f'#{tc} {mx_sc}')