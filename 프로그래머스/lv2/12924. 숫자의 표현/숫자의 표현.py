def solution(n):
    cnt = 0
    for i in range(1, n+1):
        ans = 0
        for j in range(i, n+1):
            ans += j
            if ans == n:
                cnt += 1
                break
            elif ans > n:
                break
    return cnt