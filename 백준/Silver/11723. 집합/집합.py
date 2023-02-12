import sys
input = sys.stdin.readline

M = int(input())
S = set()
for i in range(M):
    cal = list(input().split())
    if cal[0] == 'add':
        S.add(int(cal[1]))
    if cal[0] == 'remove':
        S.discard(int(cal[1]))
    if cal[0] == 'check':
        if int(cal[1]) in S:
            print(1)
        else:
            print(0)
    if cal[0] == 'toggle':
        if int(cal[1]) in S:
            S.discard(int(cal[1]))
        else:
            S.add(int(cal[1]))
    if cal[0] == 'all':
        S = set([j for j in range(1, 21)])
    if cal[0] == 'empty':
        S.clear()