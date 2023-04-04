def solution(triangle):
    ans = 0
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 앞인 경우
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            # 맨 끝인 경우
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            # 중간
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
                
    ans = max(triangle[-1])
    return ans