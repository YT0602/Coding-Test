T = int(input())
for tc in range(1, T + 1):
    cnt = [0] * 5001  # 정류장별 지나는 횟수 리스트
    N = int(input())
    for i in range(N):
        start, end = map(int, input().split())
        for i in range(start, end + 1):  # 버스 노선구간 횟수 1 증가
            cnt[i] += 1
    P = int(input())
    result = []
    for j in range(P):  # 정류장별 횟수 리스트에 추가
        station = int(input())
        result.append(cnt[station])

    print(f'#{tc}', *result)