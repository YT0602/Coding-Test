import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K+1)
coin = []
for i in range(N):
    coin.append(int(input()))


dp[0] = 1
for i in coin:
    for j in range(i, K+1):
        # coin원 동전으로 j원 만들기 -> j - coin원을 만든 후 coin원을 추가하는 것과 같음
        # 즉, coin원으로 동전을 만드는 경우의 수 -> dp[j - coin]원
        possible = dp[j-i]
        dp[j] += possible

print(dp[K])