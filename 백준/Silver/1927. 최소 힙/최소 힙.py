import sys
import heapq
input = sys.stdin.readline

N = int(input())
h = []
cnt = 0
for i in range(N):
    num = int(input())
    if num == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)