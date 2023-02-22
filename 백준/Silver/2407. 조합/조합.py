import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0] * 101

dp[0] = 0
dp[1] = 1
for i in range(2, 101):
    dp[i] = i * dp[i - 1]
print(dp[N] // (dp[M] * dp[N - M]))