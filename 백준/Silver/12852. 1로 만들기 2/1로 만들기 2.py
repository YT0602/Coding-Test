import sys
input = sys.stdin.readline


N = int(input())
# 지나온 숫자들을 함께 기록
dp = [[0, []] for _ in range(N+1)]
dp[1][0] = 0
dp[1][1] = [1]
# DP
# 1에서 1 만들기는 0회 이므로 2부터 시작
for i in range(2, N+1):
    # i-1 은 i에서 1빼는 연산 1회 해야하므로 dp[i-1]+ 1
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    # 2로 나누어떨어진다면 i를 1로 만들기는
    # i를 2로 나눈 수를 1로 만드는 연산 + 2로 나누기 연산(1회)와 같다
    # 1빼는 방법과 나누기 중에 작은 횟수 선택
    if i % 2 == 0:
        if dp[i][0] > dp[i//2][0] + 1:
            dp[i][0] = dp[i//2][0]+1
            dp[i][1] = dp[i//2][1] + [i]
    if i % 3 == 0:
        if dp[i][0] > dp[i // 3][0] + 1:
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = dp[i // 3][1] + [i]
# 최소 연산 횟수 출력
print(dp[N][0])
ans = reversed(dp[N][1])
print(*ans)