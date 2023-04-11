def solution(m, n, puddles):
    global ans
    ans = 0
    arr = [[1] * m for _ in range(n)]
    # 물웅덩이 설정
    for x, y in puddles:
        arr[y-1][x-1] = 0
    # 0행 or 0열에 물웅덩이 있으면 그 뒤로는 못감
    for i in range(m):
        if arr[0][i] == 0:
            for j in range(i+1, m):
                arr[0][j] = 0
            break
    for i in range(n):
        if arr[i][0] == 0:
            for j in range(i+1, n):
                arr[j][0] = 0
            break
        
    # 두방향으로만 탐색
    move = ((1, 0), (0, 1))
    x = 1_000_000_007
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] != 0:
                arr[i][j] = (arr[i-1][j] % x) + (arr[i][j-1] % x)
                

    ans = arr[n-1][m-1] % x
    
    return ans