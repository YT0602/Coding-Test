T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    cnt = [0] * 10  # 출현 횟수 리스트
    for i in cards:  # 해당 숫자의 인덱스 원소 1 증가
        cnt[i] += 1
    many = 0  # 최대 출현 횟수
    most = 0  # 최대 출현 숫자
    for idx, num in enumerate(cnt):
        if num >= many:  # 출현 횟수가 더 크면
            many = num  # 최대 횟수 갱신
            most = idx  # 최대 수 갱신
    print(f'#{tc} {most} {many}')