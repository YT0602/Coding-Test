T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = [0] * 5  # a, b, c, d, e
    while N % 11 == 0:  # 큰 수 부터 지수 구하기
        x[-1] += 1  # 나누어 떨어지지 않을때까지 계산
        N //= 11
    while N % 7 == 0:
        x[-2] += 1
        N //= 7
    while N % 5 == 0:
        x[-3] += 1
        N //= 5
    while N % 3 == 0:
        x[-4] += 1
        N //= 3
    while N % 2 == 0:
        x[-5] += 1
        N //= 2
    print(f'#{tc} {x[0]} {x[1]} {x[2]} {x[3]} {x[4]}')