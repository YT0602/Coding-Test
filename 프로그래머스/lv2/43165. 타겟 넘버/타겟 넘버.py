
def solution(numbers, target):
    ans = 0
    
    def DFS(n, cnt):
        global ans
        if n == len(numbers):
            if cnt == target: return 1
            else: return 0
        return DFS(n+1, cnt + numbers[n]) + DFS(n+1, cnt - numbers[n])
    
    ans = DFS(0, 0)
          
    return ans



    