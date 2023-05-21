N, K = map(int, input().split())
coin = []
for i in range(N):
    cnt = int(input())
    coin.append(cnt)

dp = [10001] * (K+1)
dp[0] = 0

for num in coin:
    for i in range(num, K+1):
        dp[i] = min(dp[i], dp[i-num]+1)
if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
