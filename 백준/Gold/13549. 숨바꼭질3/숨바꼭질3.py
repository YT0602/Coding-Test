import sys
import heapq
input = sys.stdin.readline


N, K = map(int, input().split())

time = 0
INF = 1e9
# 이동시간
v = [INF] * 100001


def seek(num):
    q = []
    heapq.heappush(q, (0, num))
    # 처음 위치는 0
    v[num] = 0
    while q:
        # 시간, 위치
        T, pos = heapq.heappop(q)
        if pos == K:
            return T
        move = [(pos*2, 0), (pos+1, 1), (pos-1, 1)]
        for i in move:
            # 최소시간 갱신
            if 0 <= i[0] < 100001 and v[i[0]] > T+i[1]:
                v[i[0]] = T+i[1]
                heapq.heappush(q, (v[i[0]], i[0]))


print(seek(N))
