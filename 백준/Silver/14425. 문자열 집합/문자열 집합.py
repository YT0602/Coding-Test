import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s_list = set()
cnt = 0
for i in range(N):
    s_list.add(input())
for _ in range(M):
    if input() in s_list:
        cnt += 1

print(cnt)
