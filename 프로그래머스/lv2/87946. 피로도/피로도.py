def solution(k, dungeons):
    global ans
    ans = -1
    l = len(dungeons)
    v = [False] * l
    
    def DFS(k, dungeons, num):
        global ans
        ans = max(ans, num)
        
        for i in range(l):
            if not v[i]:
                if k >= dungeons[i][0]:
                    v[i] = True
                    DFS(k - dungeons[i][1], dungeons, num+1)
                    v[i] = False
                    
                
    DFS(k, dungeons, 0)
    return ans