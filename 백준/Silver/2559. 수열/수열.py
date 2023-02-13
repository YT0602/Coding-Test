import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
ans = sum(numbers[:K])
mx = ans

for j in range(K, N):
    ans += numbers[j] - numbers[j-K]
    mx = max(ans, mx)

print(mx)