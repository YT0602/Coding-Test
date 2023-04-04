from collections import deque
import math

def solution(progresses, speeds):
    ans = []
    day = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        while progresses:
            progresses[0] += speeds[0] * day
            if progresses[0] >= 100:
                cnt += 1
                progresses.popleft()
                speeds.popleft()
            else:
                break
                
        if cnt != 0:
            ans.append(cnt)
            
        if progresses:
            per = 100 - progresses[0]
            day += math.ceil(per / speeds[0])


    return ans