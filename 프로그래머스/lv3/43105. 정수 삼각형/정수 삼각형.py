def solution(triangle):
    ans = 0
    dp = [[0] * i for i in range(1, len(triangle)+1)]
    # 꼭대기 값 설정
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 앞인 경우
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            # 맨 끝인 경우
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 중간
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])
                
    ans = max(dp[-1])
    return ans