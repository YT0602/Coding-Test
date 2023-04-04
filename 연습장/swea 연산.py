from collections import deque


def calcul(num):
    q = deque([num])
    while q:
        cur = q.popleft()
        for i in (cur*2, cur+1, cur-1, cur - 10):
            if i == M:
                dp[i] = dp[cur] + 1
                return
            if 0 < i <= 1000000 and dp[i] == 0:
                dp[i] = dp[cur] + 1
                q.append(i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    dp = [0] * 1000001
    calcul(N)

    print(f'#{tc} {dp[M]}')