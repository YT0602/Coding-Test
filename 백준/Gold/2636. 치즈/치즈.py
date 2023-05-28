from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0


def BFS():
    q = deque()
    q.append((0, 0))
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    melt = []

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci + move[i][0], cj + move[i][1]

            if 0 <= ni < N and 0 <= nj < M:
                if visit[ni][nj] == 0:
                    visit[ni][nj] = 1
                    # 치즈면 녹일 리스트에 추가
                    if arr[ni][nj] == 1:
                        melt.append((ni, nj))
                    # 외부면 계속 진행
                    else:
                        q.append((ni, nj))
    for x, y in melt:
        arr[x][y] = 0
    return len(melt)


# 녹일 치즈 있는지 체크
def cheese():
    for i in range(N):
        if sum(arr[i]):
            return True
    else:
        return False


cnt = 0
while cheese():
    cnt = BFS()
    ans += 1

print(ans)
print(cnt)
