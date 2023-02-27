import sys
input = sys.stdin.readline

N, K = map(int, input().split())

wei = []
val = []
dp = [0] * (K+1)

for i in range(N):
    W, V = map(int, input().split())
    wei.append(W)
    val.append(V)

for i in range(N):
    for j in range(K, 0, -1):
        if j >= wei[i]:
            dp[j] = max(dp[j], dp[j - wei[i]] + val[i])
print(dp[K])