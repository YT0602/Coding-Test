from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0


def BFS():
    q = deque()
    q.append((0, 0))
    visit = [[-1] * M for _ in range(N)]
    visit[0][0] = 0

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci + move[i][0], cj + move[i][1]

            if 0 <= ni < N and 0 <= nj < M:
                if visit[ni][nj] == -1:
                    # 치즈면 맞닿는 몇 추가
                    if arr[ni][nj] >= 1:
                        arr[ni][nj] += 1
                    # 외부면 계속 진행
                    else:
                        visit[ni][nj] = 0
                        q.append((ni, nj))

# 녹일 치즈 있는지 체크
def cheese():
    for i in range(N):
        if sum(arr[i]):
            return True
    else:
        return False


while cheese():
    BFS()
    flag = False

    for i in range(N):
        for j in range(M):
            # 맞닿는 면 2개 이상인 치즈 제거
            if arr[i][j] >= 3:
                arr[i][j] = 0
                flag = True
            # 아니면 원상복구
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if flag:
        ans += 1

print(ans)
