import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
# 겨울에 추가되는 양분 배열
arr = [list(map(int, input().split())) for _ in range(N)]
# 초기 양분 배열
energy = [[5]*N for _ in range(N)]
# 나무 심는 배열
tree = [[[] * N for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
# 초기 나무위치 입력
for i in range(M):
    r, c, age = map(int, input().split())
    tree[r-1][c-1].append(age)


# 봄-여름
def spring():
    for i in range(N):
        for j in range(N):
            # 위치에 나무가 심겨있으면
            if tree[i][j]:
                # 어린거부터 양분 먹기 위해 정렬
                tree[i][j].sort()
                # 살아있는 나무
                live = []
                # 죽은 나무 양분
                die = 0
                for lev in tree[i][j]:
                    # 양분 먹을수 있으면 먹고 양분 차감, 성장
                    if energy[i][j] >= lev:
                        energy[i][j] -= lev
                        lev += 1
                        live.append(lev)
                    # 못 먹으면 죽음
                    else:
                        die += lev//2
                # 죽은 나무 양분 추가
                energy[i][j] += die
                # 살아있는 나무 갱신
                tree[i][j] = live


# 가을-겨울
def fall():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for lev in tree[i][j]:
                    # 나무 레벨이 5의 배수면 팔방으로 나무 생성
                    if lev % 5 == 0:
                        for l in range(8):
                            nx = i + dx[l]
                            ny = j + dy[l]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)
            # 겨울에 양분 추가
            energy[i][j] += arr[i][j]


# K년 동안 반복
for i in range(K):
    spring()
    fall()
cnt = 0
# 나무 개수 카운트
for i in range(N):
    for j in range(N):
        cnt += len(tree[i][j])

print(cnt)
