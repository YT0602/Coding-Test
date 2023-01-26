import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for i in range(1, N+1):
    q.append(i)

while len(q) > 1: # 큐 원소개수가 1개 넘는동안 반복
    q.popleft() # 왼쪽에서 한개 삭제
    q.append(q.popleft()) # 왼쪽에서 한개 삭제 후 추가

print(*q)