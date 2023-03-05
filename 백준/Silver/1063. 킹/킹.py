def toPos(st):
    return int(st[1]), ord(st[0])-ord('A')+1

def toAB(i, j):
    return chr((j-1)+ord('A'))+str(i)


K, S, N = input().split()
ci, cj = toPos(K)
si, sj = toPos(S)
N = int(N)
dct = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}

for i in range(N):
    di, dj = dct[input()]
    ni, nj = ci + di, cj + dj
    if 1 <= ni <= 8 and 1 <= nj <= 8:  # 범위 내
        if (ni, nj) == (si, sj):
            if 1 <= si + di <= 8 and 1 <= sj + dj <= 8:  # 돌 이동 범위 내
                si, sj = si + di, sj + dj
                ci, cj = ni, nj
        else:
            ci, cj = ni, nj

print(toAB(ci, cj))
print(toAB(si, sj))