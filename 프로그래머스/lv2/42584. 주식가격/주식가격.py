from collections import deque

def solution(prices):
    ans = []
    x = len(prices)
    for i in range(x):
        cnt = 0
        for j in range(i, x-1):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                
                break
        ans.append(cnt)
                
    return ans
