N = int(input())
elec = []
dp = [1] * N
for _ in range(N):
    elec.append(list(map(int, input().split())))

elec.sort()

# 가장 긴 증가하는 부분수열 찾기
for i in range(1, N):
    for j in range(i):
        if elec[i][1] > elec[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))