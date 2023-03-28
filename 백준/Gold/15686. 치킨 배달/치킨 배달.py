import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 치킨집 좌표 리스트
ck = []
# 집 좌표 리스트
home = []
mn_cnt = 9999

for i in range(N):
    for j in range(N):
        # 집, 치킨집 좌표 추가
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            ck.append([i, j])


# 치킨집 중에 M개 고르는 경우의 수
for chicken in combinations(ck, M):
    cnt = 0
    # 각 집마다
    for hx, hy in home:
        dis = []
        # 각 치킨집까지의 거리 추가
        for cx, cy in chicken:
            dis.append(abs(hx-cx)+abs(hy-cy))
        # 가장 가까운 치킨거리 카운트
        cnt += min(dis)
    # 최솟값 갱신
    mn_cnt = min(cnt, mn_cnt)

print(mn_cnt)