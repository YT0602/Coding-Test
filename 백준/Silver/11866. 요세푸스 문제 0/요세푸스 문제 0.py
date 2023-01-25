from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
q = deque()
result = []

for i in range(1, N+1):
    q.append(i)

while q:
    for i in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

print(f'<{", ".join(map(str, result))}>')