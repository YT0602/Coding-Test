N = int(input())
score = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N+1)]

if N == 1:
    print(score[0])
elif N == 2:
    print(score[0] + score[1])
else:
    dp[1] = score[0]
    dp[2] = score[0] + score[1]
    dp[3] = max(score[2] + score[0], score[2] + score[1])
    for i in range(3, N+1):
        dp[i] = max(score[i-1] + score[i-2] + dp[i-3], score[i-1] + dp[i-2])
    print(dp[N])
