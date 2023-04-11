def solution(begin, target, words):
    ans = 9999
    v = [0] * len(words)
    
    def DFS(w, target, cnt):
        nonlocal ans
        if w == target:
            ans = min(cnt, ans)
            return
        
        for i in range(len(words)):
            num = 0
            for j in range(len(w)):
                if w[j] != words[i][j]:
                    num += 1
            # 교환 안했고 한글자만 다르면 교환
            if v[i] == 0 and num == 1:
                v[i] = 1
                DFS(words[i], target, cnt + 1)
                v[i] = 0
        
    
    if target in words:
        DFS(begin, target, 0)
    else:
        ans = 0
        
    return ans