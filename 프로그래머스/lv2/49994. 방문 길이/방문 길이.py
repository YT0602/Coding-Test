def solution(dirs):
    ans = 1
    move = {'L' : (0, -1), 'U' : (-1, 0), 'R': (0, 1), 'D' : (1, 0)}
    arr = [[0] * 11 for _ in range(11)]
    ci, cj = 5, 5
    v = set()
    for i in dirs:
        ni, nj = ci + move[i][0], cj + move[i][1]
        if 0 <= ni < 11 and 0 <= nj < 11:
            v.add((ci, cj, ni, nj))
            v.add((ni, nj, ci, cj))
            ci, cj = ni, nj
    if len(v) % 2:
        ans = len(v) // 2 + 1
    else:
        ans = len(v)  // 2
    
    return ans