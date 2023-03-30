def elec(num, cnt):
    # 위치가 종점 이상이면 반환
    if num >= N-1:
        return
    # 갈 수 있는 최대거리부터 탐색
    for i in range(charge[num], 0, -1):
        if num+i <= N:
            if dp[num+i] == 0 or dp[num+i] > cnt + 1:
                dp[num+i] = cnt + 1
                elec(num+i, dp[num+i])


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    # 정류장 수
    N = numbers[0]
    # 정류장 별 배터리 용량
    charge = numbers[1:]

    dp = [0] * (N+1)
    dp[0] = 0
    elec(0, -1)

    print(f'#{tc} {dp[N-1]}')