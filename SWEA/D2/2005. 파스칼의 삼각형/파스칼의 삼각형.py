T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = 0
    print(f'#{tc}')
    while n < N:
        if n == 0:
            dp = [1 for _ in range(n+1)]
        elif n == 1:
            dp = [1 for _ in range(n+1)]
        elif n > 1:
            dp2 = [1 for _ in range(n+1)]
            for i in range(1, n):
                dp2[i] = dp[i-1] + dp[i]
            dp = dp2
        n += 1
        print(*dp)