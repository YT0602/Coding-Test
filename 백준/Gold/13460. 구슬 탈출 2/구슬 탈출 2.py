from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
v = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque()
ri = rj = bi = bj = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ri, rj = i, j
        if board[i][j] == 'B':
            bi, bj = i, j

move = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = -1


def roll(r, c, dir):
    roll_cnt = 0
    # 다음위치가 벽이 아니고 현재위치가 구멍이 아니면 계속 이동
    while board[r + move[dir][0]][c + move[dir][1]] != '#' and board[r][c] != 'O':
        r += move[dir][0]
        c += move[dir][1]
        roll_cnt += 1
    return r, c, roll_cnt


def BFS(ri, rj, bi, bj):
    global ans
    q.append([ri, rj, bi, bj, 0])
    while q:
        ri, rj, bi, bj, cnt = q.popleft()
        v[ri][rj][bi][bj] = True
        # 10번해도 성공못하면 종료
        if cnt >= 10:
            break
        # 네방향으로 굴려보기
        for i in range(4):
            nri, nrj, rcnt = roll(ri, rj, i)
            nbi, nbj, bcnt = roll(bi, bj, i)

            if board[nbi][nbj] != 'O':
                # 빨간공만 구멍이면 성공
                if board[nri][nrj] == 'O':
                    ans = cnt + 1
                    return

                # 겹쳤을때는 더 많이 움직인 공 한칸 뒤로
                if nbi == nri and nbj == nrj:
                    if rcnt > bcnt:
                        nri -= move[i][0]
                        nrj -= move[i][1]
                    else:
                        nbi -= move[i][0]
                        nbj -= move[i][1]

                if not v[nri][nrj][nbi][nbj]:
                    v[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, cnt + 1])


BFS(ri, rj, bi, bj)
print(ans)

