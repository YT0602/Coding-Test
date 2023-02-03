T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    """
    D: 두 기차 전면부 사이 거리
    A: A 기차 속력
    B: B 기차 속력
    F: 파리의 속력
    """
    time = D / (A+B)
    dis = F * time
    print(f'#{tc} {dis}')