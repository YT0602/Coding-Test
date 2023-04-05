from collections import deque

def solution(n, m, x, y, r, c, k):
    dir = ['d', 'l', 'r', 'u']
    move = ((1, 0), (0, -1), (0, 1), (-1, 0))
    str = [[''] * m for _ in range(n)]
    
    q = deque()
    q.append([x-1, y-1, 0])
    
    def BFS():
        while q:
            ci, cj, cnt = q.popleft()

            if cnt >= k:
                return

            for i in range(4):
                ni = ci + move[i][0]
                nj = cj + move[i][1]
                
                if [ni, nj] == [r-1, c-1]:
                    if (cnt+1 - k) % 2:
                        return
                    else:
                        if cnt+1 == k:
                            str[ni][nj] = str[ci][cj] + dir[i]
                            return
                        
                if 0 <= ni < n and 0 <= nj < m:
                    if abs(ni - (r-1)) + abs(nj - (c-1)) + cnt + 1 > k:
                        continue
                    str[ni][nj] = str[ci][cj] + dir[i]
                    q.append([ni, nj, cnt+1])
                    break         
                                        

    if abs((abs(x-r) + abs(y-c))-k) != 1:
        BFS()
    ans = str[r-1][c-1]
    if len(ans) != k:
        ans = 'impossible'
    print(str)

    return ans