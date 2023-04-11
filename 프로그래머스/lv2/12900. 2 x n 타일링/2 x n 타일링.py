def solution(n):
    ans = 0
    x = 1_000_000_007
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] % x)+ (dp[i-2] % x)
    
    return dp[n] % x