def solution(routes):
    ans = 1
    routes.sort()
    tmp = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > tmp:
            ans += 1
            tmp = routes[i][1]
        tmp = min(tmp, routes[i][1])
    

    return ans
