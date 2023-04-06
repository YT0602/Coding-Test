from collections import deque

def solution(arr):
    n = len(arr)
    m = len(arr[0])
    ans = -1
    
    q = deque()
    q.append([0, 0])
    
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    v = [[0] * m for _ in range(n)]
    v[0][0] = 1
    
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci + move[i][0], cj + move[i][1]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 0:
                if v[ni][nj] == 0:
                    v[ni][nj] = v[ci][cj] + 1
                    q.append([ni, nj])
                
    if v[n-1][m-1] != 0:
        ans = v[n-1][m-1]

    return ans