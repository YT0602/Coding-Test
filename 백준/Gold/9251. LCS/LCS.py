import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
dp = [0] * 1000

for i in range(len(s1)):
    mx = 0
    for j in range(len(s2)):
        if mx < dp[j]:
            mx = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = mx + 1
        # mx = max(dp[j], mx)

print(max(dp))