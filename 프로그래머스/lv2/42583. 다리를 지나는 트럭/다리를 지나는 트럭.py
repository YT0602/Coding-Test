from collections import deque

def solution(bridge, weight, truck):
    ans = 0
    now = [0] * bridge
    now = deque(now)
    truck = deque(truck)
    sm = 0
    while now:
        ans += 1
        x = now.popleft()
        sm -= x
        if truck:
            if sm + truck[0] <= weight:
                y = truck.popleft()
                now.append(y)
                sm += y
            else:
                now.append(0)
    
    return ans