import heapq
import sys
input = sys.stdin.readline


N = int(input())
lac = []
cnt = 1

for i in range(N):
    S, E = map(int, input().split())
    lac.append((S, E))
lac.sort()
room = []
# 우선순위 큐 사용
# 큐의 가장 앞의 시간 보다 강의가 일찍 시작하면 강의실 추가
# 늦게 시작하면 pop후 해당 강의 끝나는 시간 추가
# 큐가 자동 정렬되기 때문에 맨 앞에는 항상 가장 일찍 끝나는 강의가 위치
heapq.heappush(room, lac[0][1])
for i in range(1, N):
    if lac[i][0] < room[0]:
        heapq.heappush(room, lac[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lac[i][1])
print(len(room))