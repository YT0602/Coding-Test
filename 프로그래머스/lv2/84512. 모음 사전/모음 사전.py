def solution(word):
    global ans
    ans = 0
    lst = ['A', 'E', 'I', 'O', 'U']
    
    def DFS(num, st, word):
        global ans
        if st == word:
            return True
        if num == 5:
            return
        for i in lst:
            ans += 1
            if DFS(num + 1, st + i, word):
                return True
            
            
    DFS(0, '', word)
    
    return ans