N = int(input())
numbers = list(map(int, input().split()))
dp = [1] * N
ans = []

# 가장 긴 증가하는 부분수열 찾기
for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

x = max(dp)
for i in range(N-1, -1, -1):
    if dp[i] == x:
        ans.append(numbers[i])
        x -= 1
ans.reverse()

print(max(dp))
print(*ans)
