import sys

input = sys.stdin.readline


N, M = map(int, input().split())
s_list = []
check = []
cnt = 0
for i in range(N):
    s_list.append(input())
for i in range(M):
    check.append(input())

for i in check:
    if i in s_list:
        cnt += 1

print(cnt)