import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 41
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3, N):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N-1]+dp[N-2], N -2)