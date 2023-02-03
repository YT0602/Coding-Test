T = int(input()) # <= 1000
for tc in range(1, T+1):
    N = int(input())
    station = [0] * 1001  # 정류장별 지나는 횟수 리스트
    for i in range(N):
        bus, S, E = map(int, input().split())
        if bus == 1:  # 일반이면 각 정류장 + 1
            for j in range(S, E+1):
                station[j] += 1
        elif bus == 2:  # 급행이면 한단계씩 띄어서 + 1
            for j in range(S, E+1, 2):
                station[j] += 1
        elif bus == 3:  # 광역이면 짝수일때 4의 배수면 + 1, 홀수면 3 배수, 10 배수 아닐때 + 1
            for j in range(S, E+1):
                if S % 2 == 0:
                    if j % 4 == 0:
                        station[j] += 1
                else:
                    if j % 3 == 0 and j % 10 != 0:
                        station[j] += 1

    print(f'#{tc} {max(station)}')