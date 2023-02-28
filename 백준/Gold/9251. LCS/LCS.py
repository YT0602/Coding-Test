import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
dp = [0] * 1000
# dp 각 문자별로 다른 문자열을 순회하면서
# 같은 문자면 + 1, 다른 경우 누적값이 해당 위치 dp보다 작으면 갱신
for i in range(len(s1)):
    mx = 0
    for j in range(len(s2)):
        if mx < dp[j]:
            mx = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = mx + 1
        # mx = max(dp[j], mx)

print(max(dp))